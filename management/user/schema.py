from typing import List

from pydantic import BaseModel, constr, EmailStr, validator

from ..location.schema import UserCountry

# from management import db
# from . import models


class User(BaseModel):
	name: constr(min_length=2, max_length=50)
	email: EmailStr

	class Config:
		orm_mode = True

	# noinspection PyMethodParameters
	@validator("email")
	def validate_abi_email(value: str):
		if value.endswith("@ab-inbev.com"):
			return value
		raise ValueError('Invalid ABI e-mail.')


class DetailedUser(BaseModel):
	id: int
	name: constr(min_length=2, max_length=50)
	email: EmailStr
	user_countries: List[UserCountry]

	class Config:
		orm_mode = True
