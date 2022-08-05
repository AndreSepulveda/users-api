from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from management.db import Base


class Country(Base):
	__tablename__ = "countries"

	country_alpha3 = Column(String(3), primary_key=True)
	alpha2 = Column(String(2))
	zone = Column(String(4))
	user_country = relationship("UserCountry", back_populates="country_details")

	def __init__(self, country_alpha3, alpha2, zone):
		self.country_alpha3 = country_alpha3
		self.alpha2 = alpha2
		self.zone = zone


class UserCountry(Base):
	__tablename__ = "user_country"

	user_country_id = Column(Integer, primary_key=True, autoincrement=True)
	user_id = Column(Integer, ForeignKey("users.id"))
	country_alpha3 = Column(String, ForeignKey("countries.country_alpha3"))
	users = relationship("User", back_populates="user_countries")
	country_details = relationship("Country")

	def __init__(self, user_id, country_alpha3):
		self.user_id = user_id
		self.country_alpha3 = country_alpha3
