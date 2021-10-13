from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://glgxilut:u12-UVGL0349qBQg8rSN-75E5bohRt3P@surus.db.elephantsql.com/glgxilut')
# engine = create_engine('sqlite:///celebs.db')
Session = sessionmaker(bind=engine)

Base = declarative_base()
