from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List
from datetime import date
from . import crud, schemas
from ..database import get_masjid_db

router = APIRouter()

@router.post("/kids/", response_model=schemas.MuhajirinKids)
def create_kid(kid: schemas.MuhajirinKidsCreate, db: Session = Depends(get_masjid_db)):
    return crud.create_kid(db=db, kid=kid)

@router.get("/kids/", response_model=List[schemas.MuhajirinKids])
def read_kids(skip: int = 0, limit: int = 10, db: Session = Depends(get_masjid_db)):
    kids = crud.get_kids(db, skip=skip, limit=limit)
    return kids

@router.post("/kids/{kid_id}/activities/", response_model=schemas.CatatanMKids)
def create_or_update_activity_for_kid(kid_id: int, activity: schemas.CatatanMKidsCreate, db: Session = Depends(get_masjid_db)):
    existing_activity = crud.get_kid_activity_by_date(db=db, kid_id=kid_id, date_created=activity.date_created)
    if existing_activity:
        return crud.update_activity(db=db, activity_id=existing_activity.id, activity=activity)
    else:
        return crud.create_activity(db=db, activity=activity, kid_id=kid_id)

@router.get("/kids/{kid_id}/activities/", response_model=List[schemas.CatatanMKids])
def get_kid_activities(
    kid_id: int,
    start_date: date = Query(...),
    end_date: date = Query(...),
    db: Session = Depends(get_masjid_db)
):
    return crud.get_kid_activities(db=db, kid_id=kid_id, start_date=start_date, end_date=end_date)

@router.get("/leaderboard/", response_model=List[schemas.LeaderboardStudent])
def get_leaderboard(
    start_date: date = Query(...),
    end_date: date = Query(...),
    db: Session = Depends(get_masjid_db)
):
    return crud.get_leaderboard(db=db, start_date=start_date, end_date=end_date)