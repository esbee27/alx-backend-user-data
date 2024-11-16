#!/usr/bin/env python3
from flask import request
from typing import List, TypeVar




class Auth:
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        if path is None or excluded_paths is None:
            return True
        if path[-1] != "/":
            path += "/"

        if path in exluded_paths:
            return False

        return False
    
    def authorization_header(self, request=None) -> str:
        if request is None:
            return None
        if request.headers.get("Authorization") is None:
            return None
        return request.headers.get("Authorization")
    
    def current_user(self, request=None) -> TypeVar("User"):
        return None

