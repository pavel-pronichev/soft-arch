import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://{user}:{pwd}@{host}/{db_name}".format(
    user=os.getenv("DB_USER", "soft_arch_user"),
    pwd=os.getenv("DB_PWD", "123456"),
    host=os.getenv("DB_HOST", "database"),
    db_name=os.getenv("DB_NAME", "softarch"))

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
