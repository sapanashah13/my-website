from sqlalchemy import Column, Integer, String
from app.db.database import Base

class ContactMessage(Base):
    __tablename__ = "contact_messages"


    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    message = Column(String)

class Event(Base):
    __tablename__ = "events"


    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)