import os
import jwt
from werkzeug.security import generate_password_hash, generate_password_hash


class User():
    """class model for User"""

    def __init__(self, username, email, password):
        """initialize variables"""
        self.username = username
        self.email = password
        self.password = password
