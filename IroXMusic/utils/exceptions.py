class AssistantErr(Exception):
    def __init__(self, error: str):
        super().__init__(f'AssistantErr: {error}')
