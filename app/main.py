from fastapi import FastAPI
from app.api.endpoints import auth, items, pick, stats

app = FastAPI(
    title="WatchReadListenAPI",
    description="Backend project for movies / songs / etc. recommender",
    version="1.5"
)

app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(items.router)
app.include_router(pick.router)
app.include_router(stats.router)

@app.get("/")
def main_menu():
    return "Welcome to Watch Read Listen API!"

