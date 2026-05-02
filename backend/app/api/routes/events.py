from fastapi import APIRouter,Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.db.database import SessionLocal
from app.db.models import Event


router = APIRouter()

#DB dependency

def get_db():
    db= SessionLocal()
    try:

        yield db
    finally:
        db.close()

#Schema
class EventForm(BaseModel):
    title: str
    description: str


 #CREATE EVENT    

@router.post("/")
def create_event(event: EventForm, db: Session = Depends(get_db)):


    new_event = Event(
        title=event.title,
        description=event.description
    )    

    db.add(new_event)
    db.commit()
    db.refresh(new_event)

    return{
        "status": "success",
        "message":"Event created",
         "id": new_event.id,
         "title": new_event.title,
         "description": new_event.description
    }



# GET ALL EVENTS
@router.get("/")
def get_events(db: Session = Depends(get_db)):

    events = db.query(Event).all()

    return events


# GET SINGLE EVENT
@router.get("/{event_id}")
def get_event(event_id: int, db: Session = Depends(get_db)):

    event = db.query(Event).filter(Event.id == event_id).first()

    if not event:
        return {"error": "Event not found"}

    return event