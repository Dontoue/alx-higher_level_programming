# Python - Classes and Objects
In this project, I began practicing object-oriented programming using classes and objects in Python. I learned about attributes, methods, and properties as well as data abstraction, data encapsulation, and information hiding.

# Tests ✔️
tests: Folder of test files.

# Tasks 📃

• 0. My first square

    ° 0-square.py: Python class Square that defines a square.

• 1. Square with size

    ° 1-square.py: Python class Square that defines a square. Builds on 0-square.py with:
        • Private instance attribute size.
        • Instantiation with size.

• 2. Size validation

    ° 2-square.py: Python class Square that defines a square. Builds on 1-square.py with:
            • Instantiation with optional size: def __init__(self, size=0):
    ° If a provided size attribute is not an integer, a TypeError exception is raised with the message must be an integer.
    ° If a provided size attribute is less than 0, a ValueError exception is raised with the message size must be >= 0.

• 3. Area of a square

    ° 3-square.py: Python class Square that defines a square. Builds on 2-square.py with:
        • Public instance attribute def area(self): that returns the current square area.

• 4. Access and update private attribute

    ° 4-square.py: Python class Square that defines a square. Builds on 3-square.py with:
        • Property def size(self): to retrieve the private instance attribute self.
        • Property setter def size(self, value): to set self.

• 5. Printing a square

    ° 5-square.py: Python class Square that defines a square. Builds on 4-square.py with:
        • Public instance method def my_print(self): that prints the square with the character # to standard output (if size == 0 -> prints an empty line).

• 6. Coordinates of a square

    ° 6-square.py: Python class Square that defines a square. Builds on 5-square.py with:
        • Private instance attribute position.
        • Property def position(self): to retreive position.
        • Property setter def position(self, value): to set position.
        • Instantiation with optional size and position: def __init__(self, size=0, position=(0, 0)):
° If a provided position attribute is not a tuple of two integers, a TypeError exception is raised with the message position must be a tuple of 2 positive integers.

• 7. Singly linked list

    ° 100-singly_linked_list.py: Python classes Node and SinglyLinkedList that define a node of a singly-linked list and a singly-linked list. The class Node is defined with:
        • Private instance attribute data.
        • Property def data(self): to set data.
        • Property setter def data(self, value): to set data.
        • Private instance attribute next_node.
        • Property def next_node(self): to set next_node.
        • Property def next_node(self, value): to set next_node.
        • Instantiation with data and next_node: def __init__(self, data, next_node=None):
    ° If a provided data attribute is not an integer, a TypeError exception is raised with the message data must be an integer.
    ° If a provided next_node attribute is not a Node or None, a TypeError exception is raised with the message next_node must be a Node object.
    ° The class SinglyLinkedList is defined with:
        • Private instance attribute head.
        • Instantiation def __init__(self):
        • Public instance method def sorted_insert(self, value): that inserts a new Node into the correct sorted position in the list increasing order).

• 8. Print Square instance

    ° 101-square.py: Python class Square that defines a square. Builds on 6-square.py with:
       • Method __str__ to set printing of a Square instance equivalent to my_print().

• 9. Compare 2 squares

    ° 102-square.py: Python class Square that defines a square. Builds on 101-square.py with:
        • Methods __eq__, __ne__, __lt__, __le__, __gt__, and __ge__, to enable usage of Square instances with logical operators ==, !=, <, <=, >, and >=, respectively, based on the square area.

• 10. ByteCode -> Python #5

    ° 103-magic_class.py: Python function matching exactly a bytecode provided by Holberton School.
