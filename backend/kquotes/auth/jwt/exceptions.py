from kquotes.auth.exceptions import BaseAuthenticationError


class AuthenticationFailed(BaseAuthenticationError):
    detail = 'Incorrect authentication credentials.'
