#!/usr/bin/env python3
from db import DB
import bcrypt
from db import User
import uuid
from sqlalchemy.orm.exc import No


def _hash_password(password: str) -> bytes:
    if type(password) != str:
        return None

    hashed_password = bcrypt.hashpw(bytes(password,"utf-8"),
    bcrypt.gensalt())
    return hashed_password

def _generate_uuid() -> str:
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        try:
            self._db.find_user_by(email=email)
            raise ValueError("User {} already exists".format(email))
        except No    
            hashed_password = _hash_password(password)
                new_user = self._db.add_user(email, hashed_password)
                return new_user("")
        
    


    def create_session(self, email: str):
        user = self._db.find_user_by(email=email)
        user.session_id = _generate_uuid()
        return user.session_id

