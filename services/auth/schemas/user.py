"""User schema definitions using Pydantic models."""

from typing import Optional
from pydantic import BaseModel, EmailStr, constr


class UserBase(BaseModel):
    """Base schema with common user attributes."""
    email: EmailStr
    username: constr(min_length=3, max_length=50)
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False


class UserCreate(UserBase):
    """Schema for creating a new user, including password."""
    password: constr(min_length=8)


class UserUpdate(BaseModel):
    """Schema for updating user information with optional fields."""
    email: Optional[EmailStr] = None
    username: Optional[constr(min_length=3, max_length=50)] = None
    password: Optional[constr(min_length=8)] = None
    is_active: Optional[bool] = None
    is_superuser: Optional[bool] = None


class UserInDB(UserBase):
    """Schema for user as stored in database, including hashed password."""
    id: int
    hashed_password: str

    class Config:
        """Pydantic configuration."""
        from_attributes = True


class UserResponse(UserBase):
    """Schema for user responses, excluding sensitive information."""
    id: int

    class Config:
        """Pydantic configuration."""
        from_attributes = True 