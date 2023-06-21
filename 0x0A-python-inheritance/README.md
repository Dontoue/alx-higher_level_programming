# Python - Inheritance
In this project, I learned about Python class inheritance. I learned about the differences between super- and sub-classes while practicing inheritance, definining classes with multiple base classes, and overiding inherited methods and attributes.

# Tests ✔️

tests: Folder of test files. Includes both -provided ones as well as the following two independently-developed:

1-my_list.txt

7-base_geometry.txt

# Function Prototypes 💾

Prototypes for functions written in this project:

# File	Prototype

0-lookup.py ----------	def lookup(obj):

2-is_same_class.py-------def is_same_class(obj, a_class):

3-is_kind_of_class.py -----	def is_kind_of_class(obj, a_class):

4-inherits_from.py-----	def inherits_from(obj, a_class):

101-add_attribute.py----	def add_attribute(obj, att, value):

# Tasks 📃

• 0. Lookup

    ° 0-lookup.py: Python function that returns a list of available attributes and methods of an objects.

• 1. My list

    ° 1-my_list.py: Python class MyList that inherits from list. Includes:
        ° Public instance method def print_sorted(self): that prints the list in ascending sorted order (assumes all list elements are ints).

• 2. Exact same object

    ° 2-is_same_class.py: Python function that returns True if an object is exactly an instance of a specified class; otherwise False.

• 3. Same class or inherit from

    ° 3-is_kind_of_class.py: Python function that returns True if an object is an instance or inherited instance of a specified class; otherwise False.

• 4. Only sub class of

    ° 4-inherits_from.py: Python function that returns True if an object is an inherited instance (either directly or indirectly) from a specified class; otherwise False.

• 5. Geometry module

    ° 5-base_geometry.py: An empty Python class BaseGeometry.

• 6. Improve Geometry

    ° 6-base_geometry.py: Python class BaseGeometry. Builds on 5-base_geometry.py with:

        ° Public instance method def area(self): that raises an Exception with the message area() is not implemented.

• 7. Integer validator

    ° 7-base_geometry.py: Python class BaseGeometry. Builds on 6-base_geometry.py with:
        ° Public instance method def integer_validator(self, name, value): that validates the parameter value.
        ° Assumes the parameter name is always a string.
        ° The parameter value must be an int, otherwise, a TypeError exception is raised with the message <name> must be an integer.
        ° The parameter value must be greater than 0, otherwise, a ValueError exception is raised with the message <value> must be greater than 0.

• 8. Rectangle

    ° 8-rectangle.py: Python class Rectangle that inherits from BaseGeometry (7-base_geometry.py). Includes:
        ° Private attributes width and height - validated with integer_validator.
        ° Instantiation with width and height: def __init__(self, width, height):

• 9. Full rectangle

    ° 9-rectangle.py: Python class Rectangle that inherits from BaseGeometry (7-base_geometry.py). Builds on 8-rectangle.py with:
        ° Implementation of the method area().
        ° Special method __str__ to print Rectangles in the format [Rectangle] <width>/<height>.

• 10. Square #1

    ° 10-square.py: Python class Square that inherits from Rectangle (9-rectangle.py). Includes:
        ° Private attribute size - validated with integer_validator.
        ° Instantiation with size: def __init__(self, size):.
        ° Implementation of the area() method.

• 11. Square #2

    ° 11-square.py: Python class Square that inherits from Rectangle (9-rectangle.py). Builds on 10-square.py with:
        ° Special method __str__ to print squares in the format [Square] <width>/<height>.

• 12. My integer

    ° 100-my_int.py: Python class MyInt that inherits from int. Includes:
        ° Inversion of the == and != operators.

• 13. Can I?

    ° 101-add_attribute.py: Python function that adds a new attribute to an object if possible.
        ° If an attribute cannot be added, a TypeError exception is raised with the message can't add new attribute
