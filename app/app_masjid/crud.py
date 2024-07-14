from datetime import date
from sqlalchemy.orm import Session
from . import models, schemas


def get_kids(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.MuhajirinKids).offset(skip).limit(limit).all()


def create_kid(db: Session, kid: schemas.MuhajirinKidsCreate):
    db_kid = models.MuhajirinKids(**kid.dict())
    db.add(db_kid)
    db.commit()
    db.refresh(db_kid)
    return db_kid


def get_kid(db: Session, kid_id: int):
    return db.query(models.MuhajirinKids).filter(models.MuhajirinKids.id == kid_id).first()


def create_activity(db: Session, activity: schemas.CatatanMKidsCreate, kid_id: int):
    db_activity = models.CatatanMKids(**activity.dict(), kid_id=kid_id)
    db.add(db_activity)
    db.commit()
    db.refresh(db_activity)
    return db_activity


def get_kid_activities(db: Session, kid_id: int, start_date: date, end_date: date):
    return db.query(models.CatatanMKids).filter(models.CatatanMKids.kid_id == kid_id, models.CatatanMKids.date_created.between(start_date, end_date)).all()


def get_badges(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Badge).offset(skip).limit(limit).all()


def create_badge(db: Session, badge: schemas.BadgeCreate):
    db_badge = models.Badge(**badge.dict())
    db.add(db_badge)
    db.commit()
    db.refresh(db_badge)
    return db_badge
