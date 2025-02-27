from fastapi import FastAPI
from app.db.database import db

app = FastAPI()


@app.on_event("startup")
async def startup():
    await db.create_all()


@app.on_event("startup")
async def startup():
    await db.create_all()

#
# graphql_app = GraphQL(schema, debug=True)
# app.add_route("/graphql", graphql_app)
# app.add_websocket_route("/graphql", graphql_app)

@app.get("/")
def health_check():
    return {"status": "OK"}
