from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .. import config

engine = create_engine(config.DATABASE_URL)
Sessionlocal = sessionmaker(autocommit= False, autoflush = False, bind = engine ).
