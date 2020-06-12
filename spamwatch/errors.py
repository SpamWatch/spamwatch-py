"""Errors returned by the API"""
from datetime import datetime

from requests import Response

from .types import Token


class SpamWatchError(Exception):
    pass


class Error(SpamWatchError):
    def __init__(self, req: Response) -> None:
        self.status_code = req.status_code
        self.text = req.text
        self.url = req.url
        Exception.__init__(self, f'code: {self.status_code} body: `{self.text}` url: {self.url}')


class UnauthorizedError(SpamWatchError):
    pass


class NotFoundError(SpamWatchError):
    pass


class Forbidden(SpamWatchError):
    def __init__(self, token: Token) -> None:
        Exception.__init__(self, f"Your tokens permission `{token.permission}` is not high enough.")


class TooManyRequests(SpamWatchError):
    until: datetime
    method: str

    def __init__(self, method, until: int) -> None:
        self.method = method
        self.until = datetime.fromtimestamp(until)
        Exception.__init__(self, f"Too Many Requests for method `{method}`. Try again in {self.until - datetime.now()}")
