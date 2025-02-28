import strawberry
from .logic import MovieService
from .schema import MovieType, MovieInput
from ..db.models import Movie


@strawberry.type
class Mutation:
    @strawberry.mutation
    async def add_movie(self, title: str, year: int, genre: str) -> MovieType:
        movie = MovieInput(genre=genre, title=title, year=year)
        return await MovieService.add_movie(movie)