from fastapi import FastAPI,APIRouter
import uvicorn
from core import config
from api import user
from api.controller.user_controller import router as user_router
from api.controller.health_controller import health_router
from api.controller.auth import auth_router
from core.database.database import init_db


app = FastAPI(name =config.base.name, version=config.base.version, description="A simple sample API", docs_url="/documentation", redoc_url=None)

@app.get("/")
async def home():
    return {"message": "Welcome to the Sample API"}

app.include_router(user_router, prefix="/users")
app.include_router(health_router, prefix="/health")
app.include_router(auth_router, prefix="/auth")



@app.on_event("startup")
async def on_startup():
    # Ensure model modules are imported so SQLModel.metadata is populated
    # before we attempt to create tables.
    await init_db()




if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, port=config.base.port, host=config.base.host)