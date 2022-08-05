from typing import Optional

from sqlalchemy.orm import Session

from . import schema
from . import models


async def verify_country_existence(country_alpha3: str, session: Session) -> Optional[schema.Country]:
	"""
	Verify if the provided alpha3 code is already registered.
	Args:
        country_alpha3: provided country alpha3 code to be checked.
        session: session object used to interact with database.

	Returns:
		Country object if alpha3 already registered.
	"""
	return session.query(models.Country).filter(models.Country.country_alpha3 == country_alpha3).first()


async def verify_user_country_existence(user_id: int, country_alpha3: str, session: Session) -> Optional[schema.Country]:
	"""
	Verify if the provided user already have the given alpha3 code.
	Args:
		user_id: id number of user to be for the country to be added.
		country_alpha3: provided country alpha3 code to be checked.
		session: session object used to interact with database.

	Returns:
		UserCountry object if alpha3 already registered.
	"""
	return session.query(models.UserCountry) \
		.filter(models.UserCountry.user_id == user_id) \
		.filter(models.UserCountry.country_alpha3 == country_alpha3) \
		.first()
