from typing import List

from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from management import db
from . import schema
from . import services
from . import validators

router = APIRouter(
	tags=['Countries'],
	prefix='/country'
)


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schema.Country)
async def create_country(request: schema.Country, session: Session = Depends(db.get_db)) -> schema.Country:
	"""
	Create a new country on database if it still doesn't exist and validations pass.
	Args:
		request: request object passed for country creation.
		session: session object used to interact with database.

	Returns:
		new country after creation.
	Raises:
		HTTPException if provided country already registered, if invalid zone or invalid country iso3.
	"""
	country = await validators.verify_country_existence(request.country_alpha3, session)

	if country:
		raise HTTPException(
			status_code=400,
			detail='Provided country already exists.'
		)

	new_country = await services.new_country_register(request, session)

	return new_country


@router.get('/', response_model=List[schema.Country])
async def get_countries(session: Session = Depends(db.get_db)) -> List[schema.Country]:
	"""
	Return a list of registered countries found at the database.
	Args:
		session: session object used to interact with database.

	Returns:
		List of registered countries found at database.
	"""
	countries = await services.get_countries(session)

	return countries


@router.delete('/{country_alpha3}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_country(country_alpha3: str, session: Session = Depends(db.get_db)) -> None:
	"""
	Remove the country with the provided alpha3 from the database.
	Args:
		country_alpha3: alpha3 code of country to be removed.
		session: session object used to interact with database.

	Returns:
		None
	"""
	return await services.delete_country(country_alpha3, session)


@router.post('/{country_alpha3}/user/{user_id}', status_code=status.HTTP_201_CREATED)
async def new_user_country(user_id: int, country_alpha3: str, session: Session = Depends(db.get_db)) -> schema.UserCountry:
	"""
	Create a new user country entrance using the provided request arguments.
	Args:
		user_id: id number of user to be for the country to be added.
		country_alpha3: alpha3 code of country to be added to the provided user.
		session: session object used to interact with database.

	Returns:
		new user country object after creation.
	"""
	user_country = validators.verify_user_country_existence(user_id, country_alpha3, session)

	if user_country:
		raise HTTPException(
			status_code=200,
			detail='Provided country_alpha3 already present for the user.'
		)
	return await services.new_user_country(user_id, country_alpha3, session)
