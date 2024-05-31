from .untyped_node import UntypedNode

class UntypedDict(UntypedNode):
    """
    Represents an untyped node with dict value.
    """

    def __init__(self, value: dict) -> None:
        """
        Creates a new instance of UntypedDict.

        Args:
            value (dict): The dict value associated with the node.
        """
        self.__value = value

    def get_value(self) -> dict:
        """
        Gets the value associated with untyped dict node.

        Returns:
            The value associated with untyped dict node.
        """
        return self.__value