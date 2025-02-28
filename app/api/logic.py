from ..db.models import Movie
from ..db.move_repository import MovieRepository
from .schema import MovieType, MovieInput


class MovieService:
    @staticmethod
    async def add_movie(movie_data: MovieInput) -> MovieType:
        movie = Movie(
            genre=movie_data.genre,
            title=movie_data.title,
            year=movie_data.year
        )
        await MovieRepository.add(movie)
        return MovieType(id=movie.id, genre=movie.genre, title=movie.title, year=movie.year)

    @staticmethod
    async def get_all_movie():
        list_of_movie = await MovieRepository.get_all()
        return [Movie(genre=movie_data.genre, title=movie_data.title, year=movie_data.year) for movie_data in list_of_movie]

    @staticmethod
    async def get_by_id(movie_id: int):
        movie_data = await MovieRepository.get_by_id(movie_id)
        return MovieType(id=movie_data.id, genre=movie_data.genre, title=movie_data.title, year=movie_data.year)

    # @staticmethod
    # async def delete(movie_id: int):
    #     await MovieRepository.delete(movie_id)
    #     return f'Successfully deleted data by id {movie_id}'
    #
    # @staticmethod
    # async def update(note_id:int, note_data: MovieType):
    #     note = Note()
    #     note.name = note_data.name
    #     note.description = note_data.description
    #     await MovieRepository.update(note_id,note)
    #
    #     return f'Successfully updated data by id {note_id}'