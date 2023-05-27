# Python - More Classes and Objects

In this project, I continued to practice object-oriented programming in Python. I learned about class methods, static methods, class vs instance attributes, and how to use the special __str__ and __repr__ methods.

# Tests ✔️

tests: Folder of test files.

# Tasks 📃

0. Simple rectangle

    ° 0-rectangle.py: Empty Python class that defines a rectangle.

1. Real definition of a rectangle

° 1-rectangle.py: Python class that defines a rectangle. Builds on 0-rectangle.py with:
    • Private instance attribute width.
    • Property getter def width(self): to get width.
    • Property setter def width(self, value): to set width.
    • Private instance attribute height.
    • Property getter def height(self): to get height.
    • Property setter def height(self, value): to set height.
    • Instantiation with optional width and height: def __init(self, width=0, height=0):
° If either of width or height is not an integer, a TypeError is raised with the message width must be an integer or height must be an integer.
° If either of width or height is less than 0, a ValueError is raised with the message width must be >= 0 or height must be >= 0.

2. Area and Perimeter

° 2-rectangle.py: Python class that defines a rectangle. Builds on 1-rectangle.py with:
    • Public instance method def area(self): that returns the area of the rectangle.
    • Public instance attribute def perimeter(self): that returns the permiter of the rectangle (if either of width or height equals 0, the perimeter is 0).

3. String representation

° 3-rectangle.py: Python class that defines a rectangle. Builds on 2-rectangle.py with:
    • Special method __str__ to print the rectangle with the # character (if either of width or height equals 0, the method returns an empty string.).

4. Eval is magic

° 4-rectangle.py: Python class that defines a rectangle. Builds on 3-rectangle.py with:
    • Special method __repr__ to return a string representation of the rectangle.

5. Detect instance deletion

° 5-rectangle.py: Python class that defines a rectangle. Builds on 4-rectangle.py with:
    • Special method __del__ that prints the message Bye rectangle... when a Rectangle is deleted.

6. How many instances

° 6-rectangle.py: Python class that defines a rectangle. Builds on 5-rectangle.py with:
    • Public class attribute number_of_instances that is initialized to 0, incremented for each new instantiation, and decremened for each instance deletion.

7. Change representation

° 7-rectangle.py: Python class that defines a rectangle. Builds on 6-rectangle.py with:
    • Public class attribute class_symbol that is initialized to # but can be any type - used as the symbol for string representation.

8. Compare rectangles

° 8-rectangle.py: Python class that defines a rectangle. Builds on 7-rectangle.py with:
    • Static method def bigger_or_equal(rect_1, rect_2): that returns the rectangle with the greater area (returns rect_1 if both areas are equal).
    • If either of rect_1 or rect_2 is not a Rectangle instance, a TypeError is raised with the message rect_1 must be an instance of Rectangle or rect_2 must be an instance of Rectangle.

9. A square is a rectangle

° 9-rectangle.py: Python class that defines a rectangle. Builds on 8-rectangle.py with:
    • Class method def square(cls, size=0): that returns a new Rectangle instance with width == height == size.

10. N Queens

° 101-nqueens.py: Python program that solves the N queens puzzle.
° Usage: ./101-nqueens.py N
° Determines all possible solutions for placing N non-attacking queens on an NxN chessboard.
° Exactly two arguments must be provided. Otherwise, the program prints Usage: nqueens N and exits with the status 1.
° If the provided N is not an integer, the program prints N must be a number and exits with the status 1.
° If the provided N is less than 4, the program prints N must be at least 4 and exits with the status 1.
° Solutions are printed one per line in the format [[r, c], [r, c], [r, c], [r, c]] where r and c represent the row and column, respectively, where a queen must be placed.
