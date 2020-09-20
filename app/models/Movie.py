"""Movie Model."""
from orator.orm import has_many

from config.database import Model
from .Crew import Crew
from .Cast import Cast
from .Genre import Genre
from .Language import Language


class Movie(Model):
    """Movie Model."""
    __table__ = 'movies'

    @has_many('movie_id', 'id')
    def casts(self):
        return Cast

    @has_many('movie_id', 'id')
    def crews(self):
        return Crew

    @has_many('movie_id', 'id')
    def genres(self):
        return Genre

    @has_many('movie_id', 'id')
    def languages(self):
        return Language
