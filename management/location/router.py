from fastapi import APIRouter, Depends, status, HTTPException, Response
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
