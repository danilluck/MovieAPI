import strawberry
from typing import List

from .schema import MovieType
from .logic import MovieService

@strawberry.type
class Query:
    @strawberry.field
    async def movies(self) -> List[MovieType]:
        return await MovieService.get_all_movie()

    @strawberry.field
    async def movie(self, movie_id: int) -> MovieType:
        return await MovieService.get_by_id(movie_id)