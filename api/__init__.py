from fastapi import APIRouter
from . import event

router = APIRouter()

router.include_router(event.router, prefix='/events', tags=['event'])