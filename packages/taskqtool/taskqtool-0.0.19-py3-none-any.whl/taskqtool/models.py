from sqlalchemy import String, Column, Integer, Boolean

from .database import Base, engine


class Task(Base):
    __tablename__ = "task"
    pid = Column("pid", String, primary_key=True, unique=True, index=True)
    startTime = Column("startTime", Integer)
    submitTime = Column("submitTime", Integer)
    running = Column("running", Boolean)
    scriptPath = Column("scriptPath", String)
    shell = Column("shell", String)

    class Config:
        orm: True


Base.metadata.create_all(bind=engine)
