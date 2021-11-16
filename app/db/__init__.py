from os import getenv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from flask import g


load_dotenv()

# connect to database using env variable
engine = create_engine(getenv('DB_URL'), echo=True, pool_size=20, max_overflow=0)
# generates temp connections to the database
Session = sessionmaker(bind=engine)
# maps the models to real mySQL tables
Base = declarative_base()

def init_db():
  Base.metadata.create_all(engine)

def get_db():
    if 'db' not in g:
        # sore db connection in app context 
        g.db = Session()

    return g.db