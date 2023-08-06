import os
import json
import warnings
from typing import Union
from getpass import getpass
from logging import getLogger
from distutils.version import StrictVersion

import requests
from beartype import beartype
from beartype.typing import Type

from cript import __api_version__
from cript import NODE_CLASSES
from cript.nodes.base import Base
from cript.nodes.primary.base_primary import BasePrimary
from cript.nodes.primary.user import User
from cript.nodes.primary.file import File
from cript.nodes.secondary.base_secondary import BaseSecondary
from cript.utils import get_api_url
from cript.utils import convert_to_api_url
from cript.utils import convert_file_size
from cript.utils import display_errors
from cript.storage_clients import GlobusClient
from cript.storage_clients import AmazonS3Client
from cript.paginator import Paginator
from cript.exceptions import APIAuthError
from cript.exceptions import APIRefreshError
from cript.exceptions import APISaveError
from cript.exceptions import APIDeleteError
from cript.exceptions import APISearchError
from cript.exceptions import APIGetError
from cript.exceptions import DuplicateNodeError
from cript.exceptions import FileSizeLimitError


logger = getLogger(__name__)


class API:
    """The entry point for interacting with the CRIPT API."""

    api_version = __api_version__
    keys = None

    def __init__(self, host: str = None, token: str = None, tls: bool = True):
        """
        Establishes a session with a CRIPT API endpoint.

        :param host: The hostname of the relevant CRIPT instance. (e.g., criptapp.org)
        :param token: The API token used for authentication.
        :param tls: Indicates whether to use TLS encryption for the API connection.
        """
        if host is None:
            host = input("Host: ")
        if token is None:
            token = getpass("API Token: ")
        self.api_url = get_api_url(host, tls)
        self.latest_api_version = None
        self.user = None
        self.storage_info = None

        self.session = requests.Session()
        self.session.headers = {
            "Authorization": token,
            "Content-Type": "application/json",
            "Accept": f"application/json; version={self.api_version}",
        }

        # Test API authentication by fetching session info and keys
        response = self.session.get(f"{self.api_url}/session-info/")
        if response.status_code == 200:
            self.latest_api_version = response.json()["latest_version"]
            self.user = self._create_node(User, response.json()["user_info"])
            self.storage_info = response.json()["storage_info"]
            API.keys = response.json()["keys"]  # For use by validators
        elif response.status_code == 404:
            raise APIAuthError("Please provide a correct base URL.")
        else:
            raise APIAuthError(display_errors(response.content))

        logger.info(f"Connection to {self.api_url} API was successful!")

        # Define storage client
        provider = self.storage_info["provider"]
        if provider == "globus":
            self.storage_client = GlobusClient(self)
        elif provider == "s3":
            self.storage_client = AmazonS3Client(self)

        # Warn user if an update is required
        if StrictVersion(self.api_version) < StrictVersion(self.latest_api_version):
            warnings.warn(response.json()["version_warning"], stacklevel=2)

    def __repr__(self):
        return f"Connected to {self.api_url}"

    def __str__(self):
        return f"Connected to {self.api_url}"

    @beartype
    def refresh(self, node: BasePrimary, max_level: int = 1):
        """
        Overwrite a node's attributes with the latest values from the database.

        :param node: The node to refresh.
        :param max_level: Max depth to recursively generate nested primary nodes.
        """
        if not isinstance(node, BasePrimary):
            raise APIRefreshError(
                f"{node.node_name} is a secondary node, thus cannot be refreshed."
            )

        if node.url:
            response = self.session.get(node.url)
            self._set_node_attributes(node, response.json())
            self._generate_nodes(node, max_level=max_level)
        else:
            raise APIRefreshError(
                "Before you can refresh a node, you must either save it or define its URL."
            )

    @beartype
    def save(
        self, node: BasePrimary, max_level: int = 1, update_existing: bool = False
    ):
        """
        Create or update a node in the database.

        :param node: The node to be saved.
        :param max_level: Max depth to recursively generate nested primary nodes.
        :param update_existing: Indicates whether to update an existing node with the same unique fields.
        """
        if not isinstance(node, BasePrimary):
            raise APISaveError(
                f"The save() method cannot be called on secondary nodes such as {node.node_name}"
            )

        if node.url:
            # Update an existing object via PUT
            response = self.session.put(url=node.url, data=node._to_json())
        else:
            # Create a new object via POST
            response = self.session.post(
                url=f"{self.api_url}/{node.slug}/", data=node._to_json()
            )

        if response.status_code in (200, 201):
            # Handle new file uploads
            if node.slug == "file" and os.path.exists(node.source):
                file_url = response.json()["url"]
                file_uid = response.json()["uid"]
                self._upload_file(file_url, file_uid, node)

            self._set_node_attributes(node, response.json())
            self._generate_nodes(node, max_level=max_level)

            # Update File node source field
            if node.slug == "file":
                self.refresh(node, max_level=max_level)

            logger.info(f"{node.node_name} node has been saved to the database.")

        else:
            try:
                # Check if a duplicate error was returned
                response_dict = json.loads(response.content)
                if "duplicate" in response_dict:
                    duplicate_url = response_dict.pop("duplicate")
                    if update_existing == True and duplicate_url is not None:
                        # Update existing duplicate node
                        node.url = duplicate_url
                        self.save(node)
                        return
                    else:
                        response_content = json.dumps(response_dict)
                        raise DuplicateNodeError(display_errors(response_content))
            except json.decoder.JSONDecodeError:
                pass
            raise APISaveError(display_errors(response.content))

    @staticmethod
    def _set_node_attributes(node, obj_json):
        """
        Set node attributes using data from an API response.

        :param node: The node you want to set attributes for.
        :param obj_json: The JSON representation of the node object.
        """
        for json_key, json_value in obj_json.items():
            setattr(node, json_key, json_value)

    @beartype
    def download_file(self, node: File, path: str = None):
        """
        Download a file from the defined storage provider.

        :param node: The `File` node object.
        :param path: Path where the file should go.
        """
        storage_provider = self.storage_info["provider"]
        if not path:
            path = f"./{node.name}"

        if isinstance(self.storage_client, GlobusClient):
            self.storage_client.https_download(node, path)
        elif isinstance(self.storage_client, AmazonS3Client):
            pass  # Coming soon

    def _upload_file(self, file_url, file_uid, node):
        """
        Upload a file to the defined storage provider.

        :param file_uid: UID of the `File` node object.
        :param file_url: URL of the `File` node object.
        :param node: The `File` node object.
        """
        # Check if file is too big
        max_file_size = self.storage_info["max_file_size"]
        file_size = os.path.getsize(node.source)
        if file_size > max_file_size:
            raise FileSizeLimitError(convert_file_size(max_file_size))

        if isinstance(self.storage_client, GlobusClient):
            self.storage_client.https_upload(file_url, file_uid, node)
        elif isinstance(self.storage_client, AmazonS3Client):
            if file_size < 6291456:
                self.storage_client.single_file_upload(file_uid, node)
            else:
                # Multipart uploads for files bigger than 6 MB
                # Ref: https://docs.aws.amazon.com/AmazonS3/latest/userguide/qfacts.html
                self.storage_client.multipart_file_upload(file_uid, node)

    def delete(self, obj: Union[BasePrimary, str, type], query: dict = None):
        """
        Delete a node in the database and clear it locally.

        :param obj: The node to be deleted itself or its class.
        :param query: A dictionary defining the query parameters (e.g., {"name": "NewMaterial"})
        """
        if isinstance(obj, BaseSecondary):
            raise APIDeleteError(
                f"The delete() method cannot be called on secondary nodes such as {obj.node_name}"
            )

        # Delete with node
        if isinstance(obj, BasePrimary):
            if obj.url:
                url = obj.url
            else:
                raise APIDeleteError(
                    f"This {obj.node_name} node does not exist in the database."
                )

        # Delete with URL
        elif isinstance(obj, str):
            url = obj
            if self.api_url not in url:
                raise APIDeleteError("Invalid URL provided.")

        # Delete with search query
        elif issubclass(obj, BasePrimary) and isinstance(query, dict):
            results = self.search(node_class=obj, query=query)
            count = results.count()
            if count == 1:
                url = results.json()[0]["url"]
            elif count < 1:
                raise APIGetError("Your query did not match any existing nodes.")
            elif count > 1:
                raise APIGetError("Your query matched more than one node.")
        else:
            raise APIDeleteError(
                "Please enter a node, valid node URL, or a node class and search query."
            )

        response = self.session.delete(url)
        if response.status_code == 204:
            # Check if node exists locally
            # If it does, clear fields to indicate it has been deleted
            local_node = self._get_local_primary_node(url)
            if local_node:
                local_node.url = None
                local_node.uid = None
                local_node.created_at = None
                local_node.updated_at = None
            logger.info("The node has been deleted from the database.")
        else:
            raise APIGetError(display_errors(response.content))

    @beartype
    def search(
        self,
        node_class: Type[BasePrimary],
        query: dict,
        limit: Union[int, None] = None,
        offset: Union[int, None] = None,
    ):
        """
        Send a query to the API and display the results.

        :param node_class: The class of the node type to query for.
        :param query: A dictionary defining the query parameters (e.g., {"name": "NewMaterial"}).
        :param limit: The max number of items to return.
        :param offset: The starting position of the query.
        :return: A `Paginator` object.
        :rtype: cript.paginator.Paginator
        """
        if not issubclass(node_class, BasePrimary):
            raise APISearchError(
                f"{node_class.node_name} is a secondary node, thus cannot be searched."
            )

        if isinstance(query, dict):
            url = f"{self.api_url}/search/{node_class.slug}/"
            payload = json.dumps(query)
            return Paginator(api=self, url=url, payload=payload, obj_class=node_class)
        else:
            raise APISearchError(f"'{query}' is not a valid query.")

    @beartype
    def get(
        self,
        obj: Union[str, Type[BasePrimary]],
        query: dict = None,
        level: int = 0,
        max_level: int = 1,
    ):
        """
        Get the JSON for a node and use it to generate a local node object.

        :param obj: The node's URL or class type.
        :param query: Search query if obj argument is a class type.
        :param level: Current nested node level.
        :param max_level: Max depth to recursively generate nested primary nodes.
        :return: The generated node object.
        :rtype: cript.nodes.Base
        """
        # Get node with a URL
        if isinstance(obj, str):
            obj = convert_to_api_url(obj)
            if self.api_url not in obj:
                raise APIGetError("Please enter a valid node URL.")
            response = self.session.get(obj)
            if response.status_code == 200:
                obj_json = response.json()
            else:
                raise APIGetError("The specified node was not found.")
            # Define node class from URL slug
            node_attr_name = obj.rstrip("/").rsplit("/")[-2].replace("-", "_")
            node_class = self._define_node_class(node_attr_name)

        # Get node with a search query
        elif issubclass(obj, BasePrimary) and query:
            results = self.search(node_class=obj, query=query)
            count = results.count()
            if count < 1:
                raise APIGetError("Your query did not match any existing nodes.")
            elif count > 1:
                raise APIGetError("Your query matched more than one node.")
            else:
                obj_json = results.json()[0]
                node_class = obj
        else:
            raise APIGetError(
                "Please enter a node URL or a node class with a search query."
            )

        # Return the local node object if it already exists
        # Otherwise, create a new node
        local_node = self._get_local_primary_node(obj_json["url"])
        if local_node:
            return local_node
        else:
            node = self._create_node(node_class, obj_json)
            self._generate_nodes(node, level=level, max_level=max_level)
            return node

    def _generate_nodes(self, node: Base, level: int = 0, max_level: int = 1):
        """
        Generate nested node objects within a given node.

        :param node: The parent node.
        :param level: Current nested node level.
        :param max_level: Max depth to recursively generate nested primary nodes.
        """
        if level <= max_level:
            level += 1

        # Limit recursive primary node generation
        skip_primary = False
        if level > max_level:
            skip_primary = True

        node_dict = node.__dict__
        for key, value in node_dict.items():
            # Skip empty values and the url field
            if not value or key == "url":
                continue

            # Generate primary nodes
            if (
                isinstance(value, str)
                and self.api_url in value
                and skip_primary == False
            ):
                # Check if node already exists in memory
                local_node = self._get_local_primary_node(value)
                if local_node:
                    node_dict[key] = local_node
                else:
                    try:
                        node_dict[key] = self.get(
                            value, level=level, max_level=max_level
                        )
                    except APIGetError:
                        # Leave the URL if node is not viewable
                        pass

            # Generate secondary nodes
            elif isinstance(value, dict):
                node_class = self._define_node_class(key)
                secondary_node = node_class(**value)
                node_dict[key] = secondary_node
                self._generate_nodes(secondary_node, level=level, max_level=max_level)

            # Define Paginator attributes
            elif isinstance(value, Paginator):
                value.api = self
                value.obj_class = self._define_node_class(key.lstrip("_"))
                value.max_level = max_level

            # Handle lists
            elif isinstance(value, list):
                for i in range(len(value)):
                    # Generate primary nodes
                    if (
                        isinstance(value[i], str)
                        and self.api_url in value[i]
                        and skip_primary == False
                    ):
                        # Check if node already exists in memory
                        local_node = self._get_local_primary_node(value[i])
                        if local_node:
                            value[i] = local_node
                        else:
                            try:
                                value[i] = self.get(
                                    value[i], level=level, max_level=max_level
                                )
                            except APIGetError:
                                # Leave the URL if node is not viewable
                                pass

                    # Generate secondary nodes
                    elif isinstance(value[i], dict):
                        node_class = self._define_node_class(key)
                        secondary_node = node_class(**value[i])
                        value[i] = secondary_node
                        self._generate_nodes(
                            secondary_node, level=level, max_level=max_level
                        )

    @staticmethod
    def _define_node_class(key: str):
        """
        Find the correct class associated with a given key.

        :param key: The key string indicating the class.
        :return: The correct node class.
        :rtype: cript.nodes.Base
        """
        for node_cls in NODE_CLASSES:
            # Use node name
            if node_cls.node_name.lower() == key.replace("_", "").lower():
                return node_cls
            # Use node list name (e.g., properties)
            if hasattr(node_cls, "list_name") and node_cls.list_name == key:
                return node_cls
        return None

    @staticmethod
    def _create_node(node_class, obj_json):
        """
        Create a node with JSON returned from the API.

        :param node_class: The class of the node to be created.
        :param obj_json: The JSON representation of the node object.
        :return: The created node.
        :rtype: cript.nodes.Base
        """
        # Pop common attributes
        url = obj_json.pop("url")
        uid = obj_json.pop("uid")
        created_at = obj_json.pop("created_at")
        updated_at = obj_json.pop("updated_at")

        # Create node
        node = node_class(**obj_json)

        # Replace common attributes
        node.url = url
        node.uid = uid
        node.created_at = created_at
        node.updated_at = updated_at

        return node

    @staticmethod
    def _get_local_primary_node(url: str):
        """
        Use a URL to get a primary node object stored in memory.

        :param url: The URL to match against existing node objects.
        :return: The matching object or None.
        :rtype: Union[cript.nodes.Base, None]
        """
        for instance in Base.__refs__:
            if hasattr(instance, "url") and url == instance.url:
                return instance
        return None
