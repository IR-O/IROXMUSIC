#!/bin/bash

# Check if the user has provided the worker name as an argument
if [ -z "$1" ]; then
  echo "Please provide a worker name as an argument."
  exit 1
fi

# Set the worker name
worker_name=$1

# Start the worker
echo "Starting worker $worker_name..."
# Add your command to start the worker here
command_to_start_worker="your_command_here"
$command_to_start_worker

# Check if the worker is running
if ! pgrep -x $worker_name > /dev/null; then
  echo "Failed to start worker $worker_name."
  exit 1
fi

echo "Worker $worker_name started successfully."

