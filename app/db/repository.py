from .database import db
from sqlalchemy.sql import select

from sqlmodel import Session
from .models import Movie

class MovieRepository:
    @staticmethod
    async def get_all():
        async with db as session:
            query = select(Movie)
            result = await session.execute(query)
            return result.scalars().all()

    @staticmethod
    async def get_by_id(movie_id: int):
        async with db as session:
            query = select(Movie).where(Movie.id == movie_id)
            result = await session.execute(query)
            movie = result.scalars().first()

    @staticmethod
    async def add(title: str, year: int, genre: str):
        async with db as session:
            async with session.begin():
                movie = Movie(title=title, year=year, genre=genre)
                session.add(movie)
            await db.commit_rollback()