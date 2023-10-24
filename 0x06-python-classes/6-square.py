#!/usr/bin/python3
"""creates a class Square."""


class Square:
    """ Square class definition
        Attributes:
            size: integer Size of square
            position: position of space and new lines as tuples
    """
    def __init__(self, size=0, position=(0, 0)):
        """initialization functn
        Args:
            size: integer size
            position: position (tuple)
        Returns:
            None
        """

        self.size = size
        self.position = position

    @property
    def size(self):
        """
        gets size, size getter
        Return:
            Size of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets size
        Args:
            value(int): size
        Raises exception
            TypeError: if size != int
            ValueError: size < 0
        Returns:
            None
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """
        gets attribute position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
            sets position
        Args:
            value(tuple): position of the square in 2D
        Returns:
            None
        """
        if len(value) != 2 or type(value) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) != int or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[1]) != int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        calculate area
        Return:
            area(int)
        """
        return self.__size ** 2

    def my_print(self):
        """
        prints a square
        Return:
            None
        """
        if self.size == 0:
            print()
        else:
            print('\n'*self.__position[1], end='')
            for i in range(self.__size):
                print(' '*self.__position[0], end='')
                print('#'*self.__size)

