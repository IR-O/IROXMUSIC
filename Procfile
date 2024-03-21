#!/bin/bash

# This is a shebang line, it specifies the interpreter that should be used to execute this script.
# In this case, the script should be executed using the bash shell.

# This comment block checks if the user has provided the worker name as an argument.
if [ -z "$1" ]; then
  # If the first argument is empty, print an error message and exit the script with a status of 1.
  # The '-z' test returns true if its argument is empty.
  # The '$1' refers to the first command-line argument passed to the script.
  echo "Please provide a worker name as an argument."
  # The 'echo' command prints the message to the standard output.
  exit 1
  # The 'exit' command causes the script to exit with a status of 1, indicating an error.
fi

# This line sets the worker name to the first command-line argument passed to the script.
worker_name=$1

# This comment block starts the worker and prints a message to the standard output.
echo "Starting worker $worker_name..."
# The 'echo' command prints the message to the standard output.
# The "$worker\_name" variable is expanded to its value.
