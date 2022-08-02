from typing import Optional

from sqlalchemy.orm import Session

from .models import User


async def verify_email_existence(email: str, session: Session) -> Optional[User]:
    """
    Verify if the provided email is already registered.
    Args:
        email: provided email to be checked.
        session: session object used to interact with database.

    Returns:
        User object if email already registered.
    """
    return session.query(User).filter(User.email == email).first()
