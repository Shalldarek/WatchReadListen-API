from fastapi import FastAPI

app = FastAPI(
    title="WatchReadListenAPI",
    description="Backend project for movies / songs / etc. recommender",
    version="1.0"
)

@app.get("/")
def main_menu():
    return "Welcome to Watch Read Listen API!"