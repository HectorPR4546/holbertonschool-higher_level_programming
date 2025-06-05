# Python - Input/Output

This project explores how to manage input/output operations in Python. You'll learn to read and write files, handle file pointers, and use JSON for object serialization. It also covers best practices like using `with` statements and documenting code properly.

---

## 📚 Learning Objectives

By the end of this project, you should be able to explain the following concepts:

- Why Python programming is awesome
- How to open and close a file properly
- How to:
  - Read the full content of a file
  - Read a file line by line
  - Move the cursor within a file
  - Write and append text to a file
- How to use the `with` statement to handle files safely
- What JSON is and how to use it
- What serialization and deserialization mean
- How to:
  - Convert a Python data structure to a JSON string
  - Convert a JSON string to a Python data structure
- How to access command-line arguments with `sys.argv`

---

## ✅ Requirements

### Python Scripts

- Allowed editors: `vi`, `vim`, `emacs`
- All files interpreted/compiled on Ubuntu 20.04 LTS using Python 3.8.5
- All files must end with a new line
- The first line of each script must be: `#!/usr/bin/python3`
- Code must follow **pycodestyle** (version 2.7.\*)
- All scripts must be executable
- File length will be tested using `wc`

### Python Test Cases

- All test files must be located in a `tests/` directory
- Test files must have a `.txt` extension
- Run tests using:
  ```bash
  python3 -m doctest ./tests/*

📁 Files and Descriptions
0-read_file.py

Reads a text file (UTF-8) and prints its content to stdout.
1-write_file.py

Writes a string to a text file (UTF-8) and returns the number of characters written.
2-append_write.py

Appends a string to the end of a text file (UTF-8) and returns the number of characters added.
3-to_json_string.py

Returns the JSON representation of a Python object (like list, dict, int, str, etc.).
4-from_json_string.py

Returns a Python object represented by a JSON string.
5-save_to_json_file.py

Writes a Python object to a text file using JSON representation.
6-load_from_json_file.py

Creates a Python object from a JSON file.
7-add_item.py

Adds all arguments from the command line to a Python list, then saves the list to a file named add_item.json.

    This file uses save_to_json_file and load_from_json_file internally. If the file doesn’t exist, it creates it.