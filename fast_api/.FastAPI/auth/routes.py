from fastapi import APIRouter, Form, Request, HTTPException
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path
import json
from auth.hashing import hash_password, verify_password

router = APIRouter()
templates = Jinja2Templates(directory=".FastAPI/templates")

DATA_FILE = Path(".FastAPI/data/users.json")

# Helper: Đọc/Ghi file JSON
def read_json():
    if not DATA_FILE.exists():
        DATA_FILE.write_text("[]")
    with DATA_FILE.open("r", encoding="utf-8") as file:
        return json.load(file)

def write_json(data):
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

# Hiển thị trang đăng ký
@router.get("/register")
def register_page(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

# Xử lý đăng ký
@router.post("/register")
def register(username: str = Form(...), password: str = Form(...)):
    users = read_json()
    if any(u["username"] == username for u in users):
        raise HTTPException(status_code=400, detail="Username already exists")
    hashed_password = hash_password(password)
    users.append({"username": username, "password": hashed_password})
    write_json(users)
    return RedirectResponse(url="/auth/login", status_code=303)

# Hiển thị trang đăng nhập
@router.get("/login")
def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

# Xử lý đăng nhập
@router.post("/login")
def login(username: str = Form(...), password: str = Form(...)):
    users = read_json()
    user = next((u for u in users if u["username"] == username), None)
    if not user or not verify_password(password, user["password"]):
        raise HTTPException(status_code=400, detail="Invalid username or password")
    return RedirectResponse(url="/todos", status_code=303)
