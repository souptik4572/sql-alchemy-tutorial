from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from base import Base

# Example of Many to One relationship
# Each actor can have multiple contact numbers but each contact number only belongs to a single actor

class ContactDetails(Base):
    __tablename__ = "contact_details"
    id = Column(Integer, primary_key=True)
    phone_number = Column(String, nullable=False)
    address = Column(String, nullable=False)

    # We are creating a foreign key actor_id which is storing the primary key of the Actor (actors) table that is id
    actor_id = Column(Integer, ForeignKey('actors.id'), nullable=False)
    # We are creating an instance of an actor which will be loaded whenever we load this particular contact number. And also the actor will also get a property contact_details which can be multiple in form of a list
    actor = relationship('Actor', backref='contact_details')

    def __init__(self, phone_number, address, actor):
        self.phone_number = phone_number
        self.address = address
        self.actor = actor