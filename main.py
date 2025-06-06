from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from urls import router_v1


def get_app() -> FastAPI:
    """
    Returns an instance of app
    """
    app = FastAPI(
        title="FastAPI Mongo",
        description="This is a simple example a FastAPI application with MongoDB.",
    )

    app.add_middleware(
        middleware_class=CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(router_v1, prefix="")

    return app


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app="main:get_app",
        host="0.0.0.0",
        port=8085,
        log_config="log_conf.yaml",
        factory=True,
    )
