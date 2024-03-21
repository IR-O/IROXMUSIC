#!/bin/bash

# Check if the user has provided the worker name as an argument
# The 'if [ -z "$1" ]; then' checks if the first argument is empty
if [ -z "$1" ]; then
  # If the first argument is empty, print an error message and exit the script with a status of 1
  echo "Please provide a worker name as an argument."
  exit 1
fi

# Set the worker name
# The 'worker_name=$1' sets the value of the first argument to the variable 'worker_name'
worker_name=$1

# Start the worker
echo "Starting worker $worker_name..."
# The command to start the worker is stored in the variable 'command_to_start_worker'
# Replace 'your_command_here' with the actual command to start the worker
command_to_start_worker="your_command_here"
# Execute the command to start the worker
$command_to_start_worker

# Check if the worker is running
# The 'pgrep -x $worker_name > /dev/null' checks if the process with the name 'worker_name' exists
if ! pgrep -x $worker_name > /dev/null; then
  # If the process does not exist, print an error message and exit the script with a status of 1
  echo "Failed to start worker $worker_name."
  exit 1
fi

# If the worker is running, print a success message
echo "Worker $worker_name started successfully."

