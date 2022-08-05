from typing import List, Optional

from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from . import schema
from . import models


async def new_country_register(request: schema.Country, session: Session) -> models.Country:
	"""
	Create a new country using the provided request arguments.
	Args:
		request: request object containing name and email.
		session: session object used to interact with database.

	Returns:
		new country object after creation.
	"""
	new_country = models.Country(
		country_alpha3=request.country_alpha3,
		alpha2=request.alpha2,
		zone=request.zone
	)
	session.add(new_country)
	session.commit()
	session.refresh(new_country)

	return new_country


async def get_countries(session: Session) -> List[models.Country]:
	"""
	Return a list of registered countries found at the database.
	Args:
		session: session object used to interact with database.

	Returns:
		List of registered countries found at database.
	"""
	countries = session.query(models.Country).all()

	return countries


async def delete_country(country_alpha3: str, session: Session) -> None:
	"""
	Remove the country with the provided alpha3 from the database.
	Args:
		country_alpha3: alpha3 code of country to be removed.
		session: session object used to interact with database.

	Returns:
		None
	"""
	session.query(models.Country).filter(models.Country.country_alpha3 == country_alpha3).delete()
	session.commit()


async def new_user_country(user_id: int, country_alpha3: str, session: Session) -> Optional[schema.UserCountry]:
	"""
	Create a new user country entrance using the provided request arguments.
	Args:
		user_id: id number of user to be for the country to be added.
		country_alpha3: alpha3 code of country to be added to the provided user.
		session: session object used to interact with database.

	Returns:
		new user country object after creation.
	"""

	try:
		user_country = models.UserCountry(
			user_id=user_id,
			country_alpha3=country_alpha3
		)
		session.add(user_country)
		session.commit()
		return user_country
	except IntegrityError:
		raise HTTPException(
			status_code=404,
			detail='Failed to add new country to the user. Please verify the provided values.'
		)
