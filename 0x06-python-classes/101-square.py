#!/usr/bin/python3
"""creates class Square."""


class Square:
    """ Square class definition
        Attributes:
            size: integer size of square
            position: position of space and new lines as tuple
    """
    def __init__(self, size=0, position=(0, 0)):
        """function initializes
        Args:
            size: integer
            position(tuple): position
        Return:
            None
        """

        self.size = size
        self.position = position

    @property
    def size(self):
        """
        gets the size
        Return:
            Square size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets size
        Args:
            value: integer size
        Raises exception
            TypeError: if size != int
            ValueError: size < 0
        Return:
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
        get position attribute
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
            sets position
        Args:
            value : position of the square in 2D space as a tuple
        Return:
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
        obtain area
        Return:
            area (int)
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

    def __str__(self):
        """
        definition of printing behavior of class
        """
        if self.__size == 0:
            return ''
        new_lines = '\n' * self.position[1]
        spaces = ' ' * self.position[0]
        hashes = '#' * self.size
        return new_lines + '\n'.join(spaces + hashes for err in range(self.size))
