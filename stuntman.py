from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship, backref
from base import Base

# Example of One to One relationship
# Each actor can have only one stunt double and also the stunt double can only work with a single actor


class Stuntman(Base):
    __tablename__ = 'stuntmen'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    active = Column(Boolean, default=True)

    # We are creating a foreign key actor_id which is storing the primary key of the Actor (actors) table that is id
    actor_id = Column(Integer, ForeignKey('actors.id'), nullable=False)
    # We are creating an instance of an actor which will be loaded whenever we load this particular stuntman. And also the actor will also get a property stuntman which is not a list
    actor = relationship("Actor", backref=backref('stuntman', uselist=False))

    def __init__(self, name, active, actor):
        self.name = name
        self.active = active
        self.actor = actor
