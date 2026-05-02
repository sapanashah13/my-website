from fastapi import APIRouter
from app.api.routes import events, contact



router = APIRouter()


router.include_router(events.router, prefix="/events", tags=["Events"])
router.include_router(contact.router, prefix="/contact", tags=["COntact"])