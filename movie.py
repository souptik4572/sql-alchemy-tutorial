from typing import Collection
from sqlalchemy import Column, String, Integer, Date, Table, ForeignKey
from sqlalchemy.orm import relationship
from base import Base

# Example of Many to Many relationship
# Every Movie is made up of multiple Actors and again an Actor can take part in multiple Movies

# Creating a new relationship table which is connecting Movie (movies) and Actor (actors) tables in a Many to Many relationship
movie_actors_association = Table(
    'movies_actors', Base.metadata,
    Column('movie_id', Integer, ForeignKey('movies.id')),
    Column('actor_id', Integer, ForeignKey('actors.id'))
)
# We can only define this relationship once, no need to metnion it again for actors table. We can also do only the converse as well in the actors.py file

# Creating the Movie Class or Movie Model

class Movie(Base):
    __tablename__ = 'movies'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    release_date = Column(Date, nullable=False)

    def __init__(self, title, release_date):
        self.title = title
        self.release_date = release_date
