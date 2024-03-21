# Define a custom exception class named 'AssistantErr' which inherits from the built-in 'Exception' class.
# This class takes a single argument 'error' during initialization, which is a string message describing the error.
# The **init** method calls the parent class's constructor and passes the formatted error message to it.
class AssistantErr(Exception):
    def __init__(self, error: str):
        super().__init__(f'AssistantErr: {error}')
