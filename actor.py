from sqlalchemy import Column, Integer, String, Date
from base import Base

# Creating the Actor Class or Actor Model

class Actor(Base):
    __tablename__ = 'actors'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    birth_date = Column(Date, nullable=False)

    def __init__(self, name, birth_date):
        self.name = name
        self.birth_date = birth_date
