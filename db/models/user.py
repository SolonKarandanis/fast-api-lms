import enum

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Enum, Text
from sqlalchemy.orm import relationship

from .mixins import Timestamp
from ..db_setup import Base


class Role(enum.IntEnum):
    teacher = 1
    student = 2

class User(Timestamp, Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(100), unique=True, index=True, nullable=False)
    username = Column(String(100), unique=True)
    password = Column(String(255))
    role = Column(Enum(Role))

    profile = relationship("Profile", back_populates="owner", uselist=False)
    student_courses = relationship("StudentCourse", back_populates="student")
    student_content_blocks = relationship(
        "CompletedContentBlock", back_populates="student")


class Profile(Timestamp, Base):
    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    bio = Column(Text, nullable=True)
    is_active = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    owner = relationship("User", back_populates="profile")