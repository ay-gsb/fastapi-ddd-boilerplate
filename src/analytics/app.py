from contextlib import asynccontextmanager

import anyio
import uvicorn
from fastapi import FastAPI

from analytics.api.routes import router
from analytics.config import settings
from analytics.infra.db import db_manager


@asynccontextmanager
async def lifespan(app: FastAPI):
    db_manager.init_engine(settings.DB_URL)

    yield

    await db_manager.close()


def create_app(lifespan_handler):
    app = FastAPI(title="Analytics API", lifespan=lifespan_handler)
    app.include_router(router)

    return app


async def run_server(task_status=anyio.TASK_STATUS_IGNORED):
    config = uvicorn.Config(
        app=create_app(lifespan),
        host=settings.APP_HOST,
        port=int(settings.APP_PORT),
        reload=True,
    )
    server = uvicorn.Server(config)

    task_status.started()

    await server.serve()


async def main_async():
    async with anyio.create_task_group() as tg:
        await tg.start(run_server)
        print("Server started successfully")


def main():
    try:
        anyio.run(main_async)
    except KeyboardInterrupt:
        print("Shutting down gracefully")
