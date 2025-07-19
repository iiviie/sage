"""User model definition."""

from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from .base import Base


class User(Base):
    """
    User model for authentication and authorization.
    
    Attributes:
        id (int): Primary key
        email (str): User's email address (unique)
        username (str): User's username (unique)
        hashed_password (str): Hashed user password
        is_active (bool): Whether the user account is active
        is_superuser (bool): Whether the user has admin privileges
    """
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)

    def __repr__(self) -> str:
        """String representation of the User model."""
        return f"<User {self.username}>" 