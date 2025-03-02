from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware


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

    return app


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app="main:get_app",
        host="0.0.0.0",
        port=8081,
        factory=True,
    )
