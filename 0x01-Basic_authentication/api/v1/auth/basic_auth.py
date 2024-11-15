#!/usr/bin/env python3

from api.v1.auth.auth import Auth

class BasicAuth:
    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        if authorization_header is None or type(authorization_header) != str:
            return None
