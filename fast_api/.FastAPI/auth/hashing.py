from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    """Mã hóa mật khẩu."""
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Kiểm tra mật khẩu có khớp không."""
    return pwd_context.verify(plain_password, hashed_password)
