from datetime import date
from actor import Actor
from movie import Movie
from contact_details import ContactDetails
from stuntman import Stuntman

from base import Session

# Creating a new session
session = Session()


def print_movie_instances(movies, message):
    print(f'\n### {message}:')
    for movie in movies:
        print(f'{movie.title} was released on {movie.release_date}')
        print("The actors are: ", end=" ")
        for actor in movie.actors:
            print(actor.name, actor.birth_date, end=' ')
        print()
    print()


# Getting all movies
movies = session.query(Movie).all()
print_movie_instances(movies, 'All movies')

# Get movies after 15-01-01
recent_movies = session.query(Movie).filter(
    Movie.release_date > date(2015, 1, 1)).all()
print_movie_instances(recent_movies, 'Recent movies')

# Get movies which have Dwayne Johnson in it
# Example of joining two tables having Many to Many releationship
dwayne_movies = session.query(Movie).join(
    Actor, Movie.actors).filter(Actor.name == 'Dwayne Johnson').all()
print_movie_instances(dwayne_movies, 'Dwayne Johnson movies')

# Get all actors who have house in Glendale
# Example of joining two tables having Many to One relationship
glendale_actors = session.query(Actor).join(ContactDetails).filter(
    ContactDetails.address.ilike('%glendale%')).all()

print('### Actors that live in Glendale:')
for actor in glendale_actors:
    print(f'{actor.name} has a house in Glendale')
print('')
