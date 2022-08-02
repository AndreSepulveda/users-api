from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from . import config


USER = config.POSTGRES_USER
PASS = config.POSTGRES_PASS
URL = config.POSTGRES_URL
DATABASE = config.POSTGRES_DATABASE_NAME


SQLALCHEMY_DATABASE_URL = f'postgresql://{USER}:{PASS}@{URL}/{DATABASE}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
	db = SessionLocal()
	try:
		yield db
	finally:
		db.close()
