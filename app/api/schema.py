import strawberry

@strawberry.type
class MovieType:
    id: int
    title: str
    year: int
    genre: str

@strawberry.input
class MovieInput:
    title: str
    year: int
    genre: str


