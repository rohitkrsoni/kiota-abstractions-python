from .untyped_node import UntypedNode

class UntypedInt(UntypedNode):
    """
    Represents an untyped node with int value.
    """
    
    def __init__(self, value: int) -> None:
        """
        Creates a new instance of UntypedInt.

        Args:
            value (bool): The int value associated with the node.
        """
        self.__value = value

    def get_value(self) -> int:
        """
        Gets the value associated with untyped int node.

        Returns:
            The value associated with untyped int node.
        """
        return self.__value