# Importing required modules
import os
import re
import sys

# Define a function to check if a given string is a valid email address
def is_valid_email(email):
    # Regular expression pattern for a valid email address
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    # Use the re.match() function to check if the email address matches the pattern
    if re.match(pattern, email):
        return True
    else:
        return False

# Define a function to check if a given file path is a valid file
def is_valid_file(file_path):
    # Check if the file path exists and is a file (not a directory)
    if os.path.isfile(file_path):
        return True
    else:
        return False

# Define a function to read the contents of a file and return it as a string
def read_file(file_path):
    # Check if the file path is a valid file
    if is_valid_file(file_path):
        # Open the file in read mode and read its contents
        with open(file_path, 'r') as file:
            contents = file.read()
        # Return the contents as a string
        return contents
    else:
        # If the file path is not valid, print an error message and exit the program
        print(f"Error: {file_path} is not a valid file.")
        sys.exit(1)

# Define a function to write the contents to a file
def write_file(file_path, contents):
    # Check if the file path is a valid file
    if is_valid_file(file_path):
        # Open the file in write mode and write the contents to it
        with open(file_path, 'w') as file:
            file.write(contents)
    else:
        # If the file path is not valid, print an error message and exit the program
        print(f"Error: {
