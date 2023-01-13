class PyRepoManagerError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return repr(self.message)


class SupportLibError(PyRepoManagerError):
    def __init__(self, message):
        super().__init__(message)


class GhModuleNotFound(PyRepoManagerError):
    def __int__(self, message):
        super().__init__(message)


class NoAuthenticatedUserError(PyRepoManagerError):
    def __int__(self, message):
        super().__init__(message)
