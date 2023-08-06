from typing import Any, List, Dict, Optional, Tuple

import drb
import numpy

import xarray
from drb import DrbNode
from drb.exceptions import DrbNotImplementationException, DrbException

from drb_driver_grib.grib_common import DrbGribAbstractNode, \
    DrbGribSimpleValueNode


class DrbGribDimNode(DrbGribAbstractNode):
    """
    This node is used to have one or many children of DrbNode but no value.

    Parameters:
        parent (DrbNode): The node parent.
        dims dimensions (dict like).
    """
    def __init__(self, parent: DrbNode, dims):
        super().__init__(parent, name='dimensions')

        self._parent: DrbNode = parent
        self._children: List[DrbNode] = []
        for key in dims.keys():
            self._children.append(DrbGribSimpleValueNode(self, key, dims[key]))

    @property
    def value(self) -> Optional[Any]:
        return None

    @property
    def attributes(self) -> Dict[Tuple[str, str], Any]:
        return {}

    def get_attribute(self, name: str, namespace_uri: str = None) -> Any:
        raise DrbException(f'Attribute not found name: {name}, '
                           f'namespace: {namespace_uri}')

    @property
    @drb.resolve_children
    def children(self) -> List[DrbNode]:
        return self._children

    def has_impl(self, impl: type) -> bool:
        return False

    def get_impl(self, impl: type, **kwargs) -> Any:
        raise DrbNotImplementationException(f'no {impl} implementation found')


class DrbGribCoordNode(DrbGribAbstractNode):
    """
    This node is used to have one or many children of DrbNode but no value.

    Parameters:
        parent (DrbNode): The node parent.
        data_set_coord (DatasetCoordinates): dataset from xarray.
    """
    def __init__(self, parent: DrbNode,
                 data_set_coord: xarray.core.coordinates.DatasetCoordinates):
        super().__init__(parent, name='coordinates')

        self._data_set_coord = data_set_coord
        self._parent: DrbNode = parent
        self._children = None

    @property
    def value(self) -> Optional[Any]:
        return self._data_set_coord

    @property
    def attributes(self) -> Dict[Tuple[str, str], Any]:
        return {}

    def get_attribute(self, name: str, namespace_uri: str = None) -> Any:
        raise DrbException(f'Attribute not found name: {name}, '
                           f'namespace: {namespace_uri}')

    @property
    @drb.resolve_children
    def children(self) -> List[DrbNode]:
        if self._children is None:
            self._children = []
            for key in self._data_set_coord.keys():
                self._children.append(DrbGribArrayNode(
                    self,
                    key,
                    self._data_set_coord[key]))
        return self._children

    def has_impl(self, impl: type) -> bool:
        return isinstance(self._data_set_coord, impl)

    def get_impl(self, impl: type, **kwargs) -> Any:
        if self.has_impl(impl):
            return self._data_set_coord
        raise DrbNotImplementationException(f'no {impl} implementation found')


class DrbGribArrayNode(DrbGribAbstractNode):
    """
    This node is used to have one or many children of DrbNode but no value.

    Parameters:
        parent (DrbNode): The node parent.
        name (str): the name of the data.
    """
    def __init__(self, parent: DrbNode,
                 name: str,
                 data_array: xarray.DataArray):
        super().__init__(parent, name=name)
        self._data_array = data_array
        self._parent: DrbNode = parent
        self._name = name
        self._attribute = None

    @property
    def value(self) -> Optional[Any]:
        return self._data_array

    @property
    def attributes(self) -> Dict[Tuple[str, str], Any]:
        if self._attribute is None:
            self._attribute = {}
            for key in self._data_array.attrs:
                self._attribute[(key, None)] = self._data_array.attrs[key]
        return self._attribute

    def get_attribute(self, name: str, namespace_uri: str = None) -> Any:
        key = (name, namespace_uri)
        if key in self.attributes.keys():
            return self.attributes[key]
        raise DrbException(f'Attribute not found name: {name}, '
                           f'namespace: {namespace_uri}')

    @property
    @drb.resolve_children
    def children(self) -> List[DrbNode]:
        return []

    def has_impl(self, impl: type) -> bool:
        if isinstance(self._data_array, impl):
            return True
        if impl == numpy.ndarray:
            return True

    def get_impl(self, impl: type, **kwargs) -> Any:
        if isinstance(self._data_array, impl):
            return self._data_array
        if impl == numpy.ndarray:
            return self._data_array.to_numpy()
        raise DrbNotImplementationException(f'no {impl} implementation found')
