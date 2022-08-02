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
	return session.query(models.Country).filter(models.Country.country_alpha3 == country_alpha3)
