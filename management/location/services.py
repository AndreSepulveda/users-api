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
