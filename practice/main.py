from fastapi import FastAPI
import uvicorn
from app.core import config,init_db
from app.api.routers.user_router import user_router



app = FastAPI()
print(config.base.reload)

@app.get("/")
def root():
    return {"message":"Welcome to practice API"}

app.include_router(user_router, prefix="/user")


@app.on_event("startup")
async def load_db():
    await init_db()


if __name__ == "__main__":
    uvicorn.run("main:app", reload=config.base.reload, port=config.base.port)