# data models (classes)
from functools import wraps
from flask import abort
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Integer
from flask_login import UserMixin, LoginManager, current_user

bcrypt = Bcrypt()
db = SQLAlchemy()
login_manager = LoginManager()

class Base(DeclarativeBase):
    pass

class Cafe(db.Model):
    __tablename__ = "cafes_database"

    id : Mapped[int] = mapped_column(primary_key=True, unique=True, nullable=False)
    name : Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    describe: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    location_url : Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    bg_url : Mapped[str] = mapped_column(String(255), nullable=False)
    cafe_url : Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    cafe: Mapped[str] = mapped_column(String(255), nullable=False)
    wifi: Mapped[str] = mapped_column(String(255), nullable=False)
    sockets: Mapped[str] = mapped_column(String(255), nullable=False)
    cafe_comments = db.relationship('Comment', back_populates='parent_cafe')


class User(db.Model, UserMixin):
    __tablename__ = "users"

    id : Mapped[int] = mapped_column(primary_key=True, unique=True, nullable=False)
    first_name: Mapped[str] = mapped_column(String(255), nullable=False)
    last_name: Mapped[str] = mapped_column(String(255), nullable=False)
    email : Mapped[str] = mapped_column(String(255), nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)

    user_comments = db.relationship('Comment', back_populates='author')

class Comment(db.Model):
    __tablename__ = "comments"

    id: Mapped[int] = mapped_column(primary_key=True, unique=True, nullable=False)
    author: Mapped[User] = db.relationship('User', back_populates='user_comments')
    parent_cafe: Mapped[Cafe] = db.relationship('Cafe', back_populates='cafe_comments')
    user_id: Mapped[int] = mapped_column(Integer, db.ForeignKey('users.id'))
    cafe_id: Mapped[int] = mapped_column(Integer, db.ForeignKey('cafes_database.id'))

    content: Mapped[str] = mapped_column(String(255), nullable=False)


def admin_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.id != 1:
            return abort(403)
        return f(*args, **kwargs)

    return decorated_function

@login_manager.user_loader
def load_user(user_id):
    return User.query.get_or_404(user_id)