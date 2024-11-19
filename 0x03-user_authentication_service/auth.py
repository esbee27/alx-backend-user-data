#!/usr/bin/env python3
from db import DB
import bcrypt


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()


    def _hash_password(password: str) -> bytes:
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        return hashed_password

    def register_user(email: str, password: str) -> user:
        user = self.-db.find_user_by(email)=email)
        if user
