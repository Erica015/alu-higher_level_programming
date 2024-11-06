#!/usr/bin/python3
class Square:
    """This is an empty class that defines a square."""
    pass

Square = __import__('0-square').Square

my_square = Square()
print(type(my_square))       # <class '0-square.Square'>
print(my_square.__dict__)    # {}

