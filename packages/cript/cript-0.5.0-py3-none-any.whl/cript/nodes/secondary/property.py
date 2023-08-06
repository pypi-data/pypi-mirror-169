from typing import Union
from logging import getLogger

from beartype import beartype

from cript.nodes.primary.base_primary import BasePrimary
from cript.nodes.primary.data import Data
from cript.nodes.primary.computation import Computation
from cript.nodes.secondary.base_secondary import BaseSecondary
from cript.nodes.secondary.condition import Condition
from cript.nodes.secondary.citation import Citation
from cript.validators import validate_key, validate_value, validate_unit


logger = getLogger(__name__)


class Property(BaseSecondary):
    """
    Object representing an observed or measured attribute
    of a `Material` or `Process` object.
    """

    node_name = "Property"
    list_name = "properties"

    @beartype
    def __init__(
        self,
        key: str,
        value: Union[str, int, float, list, None] = None,
        unit: Union[str, None] = None,
        type: Union[str, None] = None,
        method: Union[str, None] = None,
        method_description: Union[str, None] = None,
        sample_preparation: Union[BasePrimary, str, None] = None,
        uncertainty: Union[float, int, None] = None,
        uncertainty_type: Union[str, None] = None,
        components: list[Union[BasePrimary, str]] = None,
        components_relative: list[Union[BasePrimary, str]] = None,
        structure: Union[str, None] = None,
        set_id: Union[int, None] = None,
        conditions: list[Union[Condition, dict]] = None,
        data: Union[Data, str, None] = None,
        computations: list[Union[Computation, str]] = None,
        citations: list[Union[Citation, dict]] = None,
        notes: Union[str, None] = None,
    ):
        super().__init__()
        self.key = key
        self.unit = unit
        self.value = value
        self.type = type
        self.method = method
        self.method_description = method_description
        self.sample_preparation = sample_preparation
        self.uncertainty = uncertainty
        self.uncertainty_type = uncertainty_type
        self.components = components if components else []
        self.components_relative = components_relative if components_relative else []
        self.structure = structure
        self.set_id = set_id
        self.conditions = conditions if conditions else []
        self.data = data
        self.computations = computations if computations else []
        self.citations = citations if citations else []
        self.notes = notes

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, value):
        self._key = validate_key("property-key", value)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = validate_value("property-key", self.key, value, self.unit)

    @property
    def unit(self):
        return self._unit

    @unit.setter
    def unit(self, value):
        self._unit = validate_unit("property-key", self.key, value)

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = validate_key("set-type", value)

    @property
    def method(self):
        return self._method

    @method.setter
    def method(self, value):
        self._method = validate_key("property-method", value)

    @property
    def uncertainty_type(self):
        return self._uncertainty_type

    @uncertainty_type.setter
    def uncertainty_type(self, value):
        self._uncertainty_type = validate_key("uncertainty-type", value)

    @beartype
    def add_components(self, component: Union[BasePrimary, dict]):
        self._add_node(component, "components")

    @beartype
    def remove_components(self, component: Union[BasePrimary, int]):
        self._remove_node(component, "components")

    @beartype
    def add_components_relative(self, component: Union[BasePrimary, dict]):
        self._add_node(component, "components_relative")

    @beartype
    def remove_components_relative(self, component: Union[BasePrimary, int]):
        self._remove_node(component, "components_relative")

    @beartype
    def add_computation(self, computation: Union[Condition, dict]):
        self._add_node(computation, "computations")

    @beartype
    def remove_computation(self, computation: Union[Condition, int]):
        self._remove_node(computation, "computations")

    @beartype
    def add_citation(self, citation: Union[Citation, dict]):
        self._add_node(citation, "citations")

    @beartype
    def remove_condition(self, condition: Union[Condition, int]):
        self._remove_node(condition, "conditions")

    @beartype
    def add_citation(self, citation: Union[Citation, dict]):
        self._add_node(citation, "citations")

    @beartype
    def remove_citation(self, citation: Union[Citation, int]):
        self._remove_node(citation, "citations")
