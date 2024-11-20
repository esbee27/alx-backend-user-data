#!/usr/bin/env python3
from db import DB
import bcrypt
from db import User


def _hash_password(password: str) -> bytes:
    if type(password) != str:
        return None
    hashed_password = bcrypt.hashpw(password.encode('utf-8'),
    bcrypt.gensalt())
    return hashed_password


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        user = self._db.find_user_by(email=email)
        if not user:
            hashed_password = _hash_password(password)
            new_user = self._db.add_user(email, hashed_password)
            return new_user
        raise ValueError
    
    

