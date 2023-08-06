import abc
from typing import Optional, List, Any, Dict, Tuple


from drb import DrbNode, AbstractNode
from drb.exceptions import DrbNotImplementationException, DrbException
from drb.path import ParsedPath

NAMESPACE_GRIB_NODE = None


class DrbGribAbstractNode(AbstractNode, abc.ABC):

    def __init__(self, parent: DrbNode, name: str):
        super().__init__()
        self._parent: DrbNode = parent
        self._name = name
        self._path = None

    @property
    def parent(self) -> Optional[DrbNode]:
        """
        Return the parent of this node if he has one otherwise None.

        Returns:
            DrbNode: The parent of this node or None.
        """
        return self._parent

    @property
    def name(self) -> str:
        """
        Return the name of the node.
        This name doesn't contain the path of the node.

        Returns:
            str: the file name
        """
        return self._name

    @property
    def namespace_uri(self) -> Optional[str]:
        """
        Not use in this implementation.

        Return:
            None
        """
        return NAMESPACE_GRIB_NODE

    def close(self) -> None:
        """
        Not use in this implementation.
        Do nothing.
        """
        pass

    @property
    def path(self) -> ParsedPath:
        """
        Returns the path of the node.

        Returns:
            ParsedPath: The path of the node.
        """
        if self._path is None:
            self._path = self.parent.path / self.name
        return self._path


class DrbGribSimpleValueNode(DrbGribAbstractNode):
    """
    This node is used to get a simple value.

    Parameters:
        parent (DrbNode): The parent of the node.
        name (str): the name of the node.
        value (any): the value.
    """
    def __init__(self, parent: DrbNode, name: str, value: any):
        super().__init__(parent, name)
        self._attributes = None
        self._value = value

    @property
    def children(self) -> List[DrbNode]:
        """
        This node as no children.

        Returns:
            List: An empty List
        """
        return []

    @property
    def attributes(self) -> Dict[Tuple[str, str], Any]:
        """
        This node as no attributes.

        Returns:
            Dict: An empty Dict
        """
        return {}

    def get_attribute(self, name: str, namespace_uri: str = None) -> Any:
        raise DrbException(f'Attribute not found name: {name}, '
                           f'namespace: {namespace_uri}')

    @property
    def value(self) -> Any:
        """
        Get the value of the node.

        Returns:
            Any: the value.
        """
        return self._value

    def has_impl(self, impl: type) -> bool:
        return False

    def get_impl(self, impl: type, **kwargs) -> Any:
        raise DrbNotImplementationException(f'no {impl} '
                                            f'implementation found')
