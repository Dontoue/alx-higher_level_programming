# Python - Input/Output
In this project, I practiced file handling in Python. I used the builtin with, open, and read functions with the json module to read and write files and serialize and deserialize objects with JSON.

# Tests ✔️
tests: Folder of test files.

# Function Prototypes 💾

Prototypes for functions written in this project:

# File	Prototype

0-read_file.py ---	def read_file(filename=""):

1-number_of_lines.py ---	def number_of_lines(filename=""):

2-read_lines.py---	def read_lines(filename="", nb_lines=0):

3-write_file.py---	def write_file(filename="", text=""):

4-append_write.py---	def append_write(filename="", text=""):

5-to_json_string.py---	def to_json_string(my_obj):

6-from_json_string.py---	def from_json_string(my_str):

7-save_to_json_file.py---	def save_to_json_file(my_obj, filename):

8-load_from_json_file.py---	def load_from_json_file(filename):

10-class_to_json.py---	def class_to_json(obj):

14-pascal_triangle.py---	def pascal_triangle(n):

100-append_after.py---	def append_after(filename="", search_string="", new_string=""):

# Tasks 📃

• 0. Read file

    ° 0-read_file.py: Python function that prints the contents of a UTF8 text file to standard output.

• 1. Number of lines

    ° 1-number_of_lines.py: Python function that returns the number of lines contained in a text file.

• 2. Read n lines

    ° 2-read_lines.py: Python function that prints n lines of a UTF8 text file to standard output.

• 3. Write to a file

    ° 3-write_file.py: Python function that writes a string to a UTF8 text file and returns the number of characters written.

• 4. Append to a file

    ° 4-append_write.py: Python function that appends a string to the end of a UTF8 text file and returns the number of characters appended.

• 5. To JSON string

    ° 5-to_json_string.py: Python function that returns the JSON string representation of an object.

• 6. From JSON string to Object

    ° 6-from_json_string.py: Python function that returns the Python object represented by a JSON string.

• 7. Save Object to a file

    ° 7-save_to_json_file.py: Python function that writes an object to a text file using JSON representation.

• 8. Create object from a JSON file

    ° 8-load_from_json_file.py: Python function that creates an object from a .json file.

• 9. Load, add, save

    ° 9-add_item.py: Python script that stores all command line arguments to a Python list saved in the file add_item.json.

• 10. Class to JSON

    ° 10-class_to_json.py: Python function that returns the dictionary description for simple Python data structures (lists, dictionaries, strings, integers and booleans).

• 11. Student to JSON

    ° 11-student.py: Python class Student that defines a student. Includes:

    ° Public instance attributes first_name, last_name, and age.

    ° Instantiation with first_name, last_name, and age: def __init__(self, first_name, last_name, age):.

    ° Public method def to_json(self): that returns the dictionary representation of a Student instance.

    ° 12. Student to JSON with filter

• 12-student.py: Python class Student that defines a student. Builds on 11-student.py with:

    ° Public method def to_json(self, attrs=None): that returns the dictionary representation of a Student instance.

    ° If attrs is a list of strings, only the attributes listed are represented in the dictionary.

• 13. Student to disk and reload

    ° 13-student.py: Python class Student that defines a student. Builds on 12-student.py with:

    ° Public method def reload_from_json(self, json): that replaces all attributes of the Student instance using the key/value pairs listed in json.

    ° The method assumes json is a dictionary containing attributes with name/value corresponding to key/value.

• 14. Pascal's Triangle

    ° 14-pascal_triangle.py: Python function that returns a list of lists of integers representing Pascal's triangle of size n.

    ° Assumes the size parameter n is an integer.

    ° If n is less than or equal to 0, returns an empty list.

• 15. Search and update

    ° 100-append_after.py: Python function that inserts a line of text to a file after each line containing a specified string.

• 16. Log parsing

    ° 101-stats.py: Python script that reads lines from standard input. After every 10 lines or the input of a keyboard interruption (CTRL + C), computes the following metrics:

    ° Total file size up that point: File size: <total size>

    ° Status code of each read line, printed in ascending order: <status code>: <number>

    ° Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>

• 17. Hack the VM

    ° read_write_heap.py: Python script that finds and replaces a string in the heap of a running process.

    ° Usage: read_write_heap.py pid search_string replace_string where pid is the process ID of the running process and strings are represented in ASCII.

    ° Only looks in the heap of the process.
    
    ° On a usage error, prints an error message to stdout and exits with the status code 1.
