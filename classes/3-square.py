class Square:
   class Square:
    """A class that defines a square by:
    - Private instance attribute: size
    - Instantiation with optional size: def init(self, size=0):
      - size must be an integer, otherwise raise a TypeError exception with the message "size must be an integer"
      - If size is less than 0, raise a ValueError exception with the message "size must be >= 0"
    """

    def init(self, size=0):
        """Initializes a new Square.

        Args:
            size (int): The size of the new Square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    def area(self):
        """Returns the area of the square."""
        return self.size * self.size