from typing import List

from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy.orm import Session

from management import db
from . import schema
from . import services
from . import validators

router = APIRouter(
	tags=['Users'],
	prefix='/user'
)


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schema.DetailedUser)
async def create_user(request: schema.User, session: Session = Depends(db.get_db)) -> schema.DetailedUser:
	"""
	Create the requested user on database if unregistered email and validations pass.
	Args:
		request: request object passed for user creation.
		session: session object used to interact with database.

	Returns:
		new user after creation.
	Raises:
		HTTPException if provided email is already registered.
	"""
	user = await validators.verify_email_existence(request.email, session)

	if user:
		raise HTTPException(
			status_code=400,
			detail='Provided email already registered.',
		)

	new_user = await services.new_user_register(request, session)

	return new_user


@router.get('/', response_model=List[schema.DetailedUser])
async def get_users(session: Session = Depends(db.get_db)) -> List[schema.DetailedUser]:
	"""
	Return a list of registered users found at the database.
	Args:
		session: session object used to interact with database.

	Returns:
		List of registered users found at database.
	"""
	return await services.get_users(session)


@router.get('/{user_id}', status_code=status.HTTP_200_OK, response_model=schema.DetailedUser)
async def get_user(user_id: int, session: Session = Depends(db.get_db)) -> schema.DetailedUser:
	"""
	Return the user with the specified id.
	Args:
		user_id: id number of user to be looked for.
		session: session object used to interact with database.

	Returns:
		Detailed user object for the provided id.
	"""
	return await services.get_user(user_id, session)


@router.delete('/{user_id}', status_code=status.HTTP_204_NO_CONTENT, response_class=Response)
async def delete_user(user_id: int, session: Session = Depends(db.get_db)) -> Response:
	"""
	Remove the user with the specified id.
	Args:
		user_id: id number of user to be removed.
		session: session object used to interact with database.

	Returns:
		Response object after running remove operation.
	"""
	return await services.delete_user(user_id, session)
