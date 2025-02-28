from fastapi import FastAPI
from app.db.database import db
import strawberry
from strawberry.fastapi import GraphQLRouter

from app.api.query import Query
from app.api.mutation import Mutation

app = FastAPI()


@app.on_event("startup")
async def startup():
    await db.create_all()


@app.on_event("startup")
async def startup():
    await db.create_all()



schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app, prefix = "/graphql")
# app.add_websocket_route("/graphql", graphql_app)

@app.get("/")
def health_check():
    return {"status": "OK"}
