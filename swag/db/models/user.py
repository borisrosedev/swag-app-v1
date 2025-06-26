from sqlalchemy import Integer, String, Enum
from sqlalchemy.orm import Mapped, mapped_column
import enum
from werkzeug.security import generate_password_hash, check_password_hash
from .. import db

class UserRole(enum.Enum):
    user = "user"
    admin = "admin"

class User(db.Model):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(255), unique=True)
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)
    firstname: Mapped[str] = mapped_column(String(100), nullable=False)
    lastname: Mapped[str] = mapped_column(String(100), nullable=False)
    role: Mapped[UserRole] = mapped_column(Enum(UserRole), nullable=False, default=UserRole.user)
    photo_url: Mapped[str] = mapped_column(String(200), nullable=False)


    def get_fullname(self):
        return f"{self.firstname.capitalize()} {self.lastname.capitalize()}"

    @property
    def password(self):
        raise AttributeError("Password is write-only.")

    @password.setter
    def password(self, raw_password):
        self.password_hash = generate_password_hash(raw_password, method="pbkdf2:sha256:600000")

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
