from pydantic import BaseModel, constr, validator


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
		raise ValueError('Invalid zone.')


class UserCountry(BaseModel):
	user_id: int
	country_alpha3: str

	class Config:
		orm_mode = True

# TODO add DisplayUserCountry to show user_country_id
