from sqlalchemy import Column, Integer, String

from management.db import Base


class User(Base):
	__tablename__ = "users"

	id = Column(Integer, primary_key=True, autoincrement=True)
	name = Column(String(50))
	email = Column(String(255))

	def __init__(self, name, email):
		self.name = name
		self.email = email
