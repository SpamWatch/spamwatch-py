"""Types returned by the API"""
from datetime import datetime
from enum import Enum, auto
from typing import Optional


class Permission(Enum):
    Root = auto()
    Admin = auto()
    User = auto()


_permission_map = {
    'Root': Permission.Root,
    'Admin': Permission.Admin,
    'User': Permission.User
}


class SpamWatchType:
    def __str__(self) -> str:
        return f'<{self.__class__.__name__}: {self.__dict__}>'

    def __repr__(self) -> str:
        return self.__str__()


class Token(SpamWatchType):
    id: int
    permission: Optional[Permission]
    token: str
    userid: int
    retired: bool

    def __init__(self, id: int, permission: str, token: str, userid: int, retired: bool, **kwargs) -> None:
        self.id = id
        self.permission = _permission_map.get(permission)
        self.token = token
        self.userid = userid
        self.retired = retired


class Ban(SpamWatchType):
    id: int
    reason: str
    date: datetime
    timestamp: int
    admin: int
    message: Optional[str]

    def __init__(self,
                 id: int,
                 reason: str,
                 admin: int,
                 date: int = 0,
                 message: Optional[str] = None,
                 **kwargs) -> None:
        self.id = id
        self.reason = reason
        self.date = datetime.fromtimestamp(date)
        self.timestamp = date
        self.admin = admin
        self.message = message
