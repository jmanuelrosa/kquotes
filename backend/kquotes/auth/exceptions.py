class BaseAuthenticationError(Exception):
    status_code = 401

    def __init__(self, detail=None):
        self.detail = detail or self.detail

    def __str__(self):
        return self.detail


class LoginNeeded(BaseAuthenticationError):
    detail = 'Login is needed'
