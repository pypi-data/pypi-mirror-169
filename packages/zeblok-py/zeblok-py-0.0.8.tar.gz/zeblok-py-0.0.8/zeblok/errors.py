class InvalidCredentialsError(Exception):
    def __init__(self, message):
        super().__init__(message)


class AuthenticationError(Exception):
    def __init__(self, message):
        super().__init__(message)


class ServerError(Exception):
    def __init__(self, message):
        super().__init__(message)


class InvalidModelFolder(Exception):
    def __init__(self, message):
        super().__init__(message)


class InvalidBaseURL(Exception):
    def __init__(self, message):
        super().__init__(message)


class InvalidStorageURL(Exception):
    def __init__(self, message):
        super().__init__(message)


class FileUploadError(Exception):
    def __init__(self, message):
        super().__init__(message)


class PipelineCreationError(Exception):
    def __init__(self, message):
        super().__init__(message)


class ModelDeploymentError(Exception):
    def __init__(self, message):
        super().__init__(message)


class BucketDoesNotExistsError(Exception):
    def __init__(self, message):
        super().__init__(message)
