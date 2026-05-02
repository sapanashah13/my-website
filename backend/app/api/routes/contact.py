from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session


from app.db.database import SessionLocal
from app.db.models import ContactMessage


router = APIRouter()
#Dependency (database connection)
def get_db():
    db = SessionLocal()
    
    try:
        yield db 
    finally:
        db.close()


#Temporary storage 

class ContactForm(BaseModel):
    name: str
    email: str
    message: str






@router.post("/")
def send_message(form: ContactForm, db:Session = Depends(get_db)):
    new_message = ContactMessage(
        name=form.name,
        email=form.email,
        message=form.message
    )
   

    db.add(new_message)
    db.commit()
    db.refresh(new_message)


    return {
        "status": "success",
        "message": "Message received successfully",
        "data": {
            "id": new_message.id,
            "name": new_message.name,
            "email": new_message.email,
            "message": new_message.message
        }
    }


@router.get("/")
def get_messages(db: Session = Depends(get_db)):
    
    messages = db.query(ContactMessage).all()
    return messages
