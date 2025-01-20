from fastapi import APIRouter, Form, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path
import json

router = APIRouter()
templates = Jinja2Templates(directory=".FastAPI/templates")
DATA_FILE = Path(".FastAPI/data/todos.json")

# Helper: Đọc/Ghi file JSON
def read_json():
    if not DATA_FILE.exists():
        DATA_FILE.write_text("[]")
    with DATA_FILE.open("r", encoding="utf-8") as file:
        return json.load(file)

def write_json(data):
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

# Hiển thị danh sách to-dos
@router.get("/todos")
def get_todos(request: Request):
    todos = read_json()
    return templates.TemplateResponse("todos.html", {"request": request, "todos": todos})

# Thêm to-do
@router.post("/todos/add")
def add_todo(title: str = Form(...), description: str = Form(...)):
    todos = read_json()
    new_todo = {"id": len(todos) + 1, "title": title, "description": description}
    todos.append(new_todo)
    write_json(todos)
    return RedirectResponse(url="/todos", status_code=303)
