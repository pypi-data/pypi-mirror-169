from typing import Union
from logging import getLogger

from beartype import beartype

from cript.nodes.primary.data import Data
from cript.nodes.secondary.base_secondary import BaseSecondary
from cript.nodes.secondary.citation import Citation
from cript.validators import validate_key


logger = getLogger(__name__)


class ComputationalForcefield(BaseSecondary):
    """
    Object representing the computational forcefield of a
    virtual `Material`.
    """

    node_name = "ComputationalForcefield"

    @beartype
    def __init__(
        self,
        key: str,
        building_block: str,
        coarse_grained_mapping: Union[str, None] = None,
        implicit_solvent: Union[str, None] = None,
        source: Union[str, None] = None,
        description: Union[str, None] = None,
        data: Union[Data, str, None] = None,
        citations: list[Union[Citation, dict]] = None,
    ):
        super().__init__()
        self.key = key
        self.description = description
        self.building_block = building_block
        self.coarse_grained_mapping = coarse_grained_mapping
        self.implicit_solvent = implicit_solvent
        self.source = source
        self.data = data
        self.citations = citations if citations else []

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, value):
        self._key = validate_key("computational-forcefield-key", value)

    @property
    def building_block(self):
        return self._building_block

    @building_block.setter
    def building_block(self, value):
        self._building_block = validate_key("building-block", value)
