from pydantic import BaseModel, constr, validator
from pycountry import countries


class Country(BaseModel):
	country_alpha3: str
	alpha2: str
	zone: constr(min_length=3, max_length=4)

	class Config:
		orm_mode = True

	# noinspection PyMethodParameters
	@validator('zone')
	def validate_zone(value: str):
		if value in ['naz', 'maz', 'saz', 'eur', 'afr', 'apac']:
			return value
		raise ValueError('Invalid zone code.')

	# noinspection PyMethodParameters
	@validator('country_alpha3')
	def validate_country_alpha3(value: str):
		if countries.get(alpha_3=value.lower()):
			return value
		raise ValueError('Invalid country alpha3.')


class UserCountry(BaseModel):
	user_id: int
	country_alpha3: str

	class Config:
		orm_mode = True

# TODO add DisplayUserCountry to show user_country_id
