"""Token schema definitions using Pydantic models."""

from typing import Optional
from pydantic import BaseModel


class Token(BaseModel):
    """Token schema."""
    access_token: str
    token_type: str


class TokenData(BaseModel):
    """Token payload schema."""
    username: Optional[str] = None 