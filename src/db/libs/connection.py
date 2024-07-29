from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from config.config import config

engine = create_engine(
    url= config['db_url'],
    pool_size=10
)

SessionLocal = sessionmaker( autocommit=False, autoflush=False, bind=engine )

Base = declarative_base()