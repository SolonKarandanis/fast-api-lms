from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel,create_engine, Session

SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://fastapi:fastapi@192.168.1.6/fastapi"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={}, future=True,echo=True
)
SessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine, future=True
)

Base = declarative_base()

# DB Utilities
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# sqlmodel
def init_db():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session

