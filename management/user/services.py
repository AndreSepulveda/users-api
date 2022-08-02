from typing import List, Optional

from fastapi import HTTPException
from sqlalchemy.orm import Session

from . import schema
from . import models


async def new_user_register(request: schema.User, session: Session) -> models.User:
	"""
	Create a new user using the provided request arguments.
	Args:
		request: request object containing name and email.
		session: session object used to interact with database.

	Returns:
		new user object after creation.
	"""
	new_user = models.User(name=request.name, email=request.email)
	session.add(new_user)
	session.commit()
	session.refresh(new_user)

	return new_user


async def get_user(user_id: int, session: Session) -> Optional[models.User]:
	"""
	Search a user with the provided it at database.
	Args:
		user_id: id number of user to be looked for.
		session: session object used to interact with database.

	Returns:
		Detailed user object for the provided id.
	Raises:
		HTTPException if provided id isn't found.
	"""
	user = session.query(models.User).filter(models.User.id == user_id).first()

	if not user:
		raise HTTPException(
			status_code=404,
			detail="The provided user_id could not be found."
		)
	return user


async def get_users(session: Session) -> List[models.User]:
	"""
	Return a list of registered users found at the database.
	Args:
		session: session object used to interact with database.

	Returns:
		List of registered users found at database.
	"""
	# TODO: Add paginate function to handle large results
	# It can be done using LIMIT, OFFSET and page number
	# or using https://pypi.org/project/paginate-sqlalchemy/
	users = session.query(models.User).all()

	return users


async def delete_user(user_id: int, session: Session):
	"""
	Remove the user with the provided id from the database.
	Args:
		user_id: id number of user to be removed.
		session: session object used to interact with database.

	Returns:
		None
	"""
	session.query(models.User).filter(models.User.id == user_id).delete()
	session.commit()
