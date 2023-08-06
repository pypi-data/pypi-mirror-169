from typing import Union
from logging import getLogger

from beartype import beartype

from cript.nodes.primary.base_primary import BasePrimary
from cript.nodes.primary.user import User


logger = getLogger(__name__)


class Group(BasePrimary):
    """Object representing a CRIPT group."""

    node_name = "Group"
    slug = "group"

    @beartype
    def __init__(
        self,
        name: str,
        users: list[Union[User, str]] = None,
        public: bool = False,
    ):
        super().__init__(public=public)
        self.name = name
        self.users = users if users else []

    @beartype
    def add_user(self, user: Union[User, dict]):
        self._add_node(user, "users")

    @beartype
    def remove_user(self, user: Union[User, int]):
        self._remove_node(user, "users")
