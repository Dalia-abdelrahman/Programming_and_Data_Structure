class Square:
    """A class that defines a square by:
    - Private instance attribute: size
    - Instantiation with size (no type/value verification)
    """

    def init(self, size):
        """Initializes a new Square.

        Args:
            size (int): The size of the new Square.
        """
        self.__size = size