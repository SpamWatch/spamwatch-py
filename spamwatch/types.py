from datetime import datetime
from enum import Enum, auto


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
    def __str__(self):
        return f'<{self.__class__.__name__}: {self.__dict__}>'

    def __repr__(self):
        return self.__str__()


class Token(SpamWatchType):
    id: int
    permission: Permission
    token: str
    userid: int

    def __init__(self, id, permission, token, userid):
        self.id = id
        self.permission = _permission_map.get(permission)
        self.token = token
        self.userid = userid


class Ban(SpamWatchType):
    id: int
    reason: str
    date: datetime
    timestamp: int

    def __init__(self, id, reason, date=0):
        self.id = id
        self.reason = reason
        self.date = datetime.fromtimestamp(date)
        self.timestamp = date
