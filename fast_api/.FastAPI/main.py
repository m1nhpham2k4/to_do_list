from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from auth.routes import router as auth_router
from todo.routes import router as todo_router


app = FastAPI()

# Static files
app.mount("/static", StaticFiles(directory=".FastAPI/static"), name="static")

# Routers
app.include_router(auth_router, prefix="/auth", tags=["Authentication"])
app.include_router(todo_router, prefix="/todos", tags=["To-Do List"])

@app.get("/")
def home():
    return RedirectResponse(url="/auth/login")
