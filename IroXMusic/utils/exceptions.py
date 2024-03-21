# Define a custom exception class named 'AssistantErr' that inherits from the built-in 'Exception' class.
# This class takes a single argument 'error' during initialization, which is a string message describing the error.
# The **init** method calls the parent class's constructor and passes the formatted error message to it.
class AssistantErr(Exception):
    def __init__(self, error: str):
        super().__init__(f'AssistantErr: {error}')


def raise_assistant_err(error_message: str):
    """Raise a custom AssistantErr with a given error message."""
    raise AssistantErr(f"An error occurred in the assistant: {error_message}")


# Example usage:
try:
    raise_assistant_err("This is a custom error for the assistant.")
except AssistantErr as e:
    print(e)
