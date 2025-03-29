# data models (classes)

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String

db = SQLAlchemy()

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