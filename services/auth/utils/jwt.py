"""JWT token handling utilities."""

from datetime import datetime, timedelta
from typing import Optional

from jose import JWTError, jwt

from ..schemas.token import Token, TokenData

# TODO: Move these to environment variables
SECRET_KEY = "your-secret-key-keep-it-secret"  # Change this!
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    """
    Create a new JWT access token.
    
    Args:
        data: Data to encode in the token
        expires_delta: Optional expiration time, defaults to 30 minutes
        
    Returns:
        Encoded JWT token as string
    """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_token(token: str, credentials_exception) -> TokenData:
    """
    Verify a JWT token and return its payload.
    
    Args:
        token: JWT token to verify
        credentials_exception: Exception to raise if verification fails
        
    Returns:
        TokenData containing the username from the token
        
    Raises:
        credentials_exception: If token is invalid
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        return TokenData(username=username)
    except JWTError:
        raise credentials_exception 