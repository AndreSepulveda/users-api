from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from management.db import Base


class User(Base):
	__tablename__ = "users"

	id = Column(Integer, primary_key=True, autoincrement=True)
	name = Column(String(50))
	email = Column(String(255))
	user_countries = relationship("UserCountry", back_populates="users")

	def __init__(self, name, email):
		self.name = name
		self.email = email
