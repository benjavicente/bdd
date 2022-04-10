from fastapi import APIRouter, Depends
from sqlmodel import Session, select

from fastapi_pagination import Page, add_pagination
from fastapi_pagination.ext.sqlmodel import paginate

from ...db import Place
from ..utils import get_db

place_router = APIRouter()


@place_router.get("/", response_model=list[Place])
async def get_places(db: Session = Depends(get_db)):
    return db.exec(select(Place)).all()


add_pagination(place_router)