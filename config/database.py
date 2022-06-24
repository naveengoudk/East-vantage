from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# url for connecting to sqlite database
SQLALCHEMY_DATABASE_URL = "sqlite:///./addresses.db"

# creting engine for connecting to sqlite database
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# creating session for connecting to sqlite database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# creating base class for creating tables
Base = declarative_base()
