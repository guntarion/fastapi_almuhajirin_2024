from sqlalchemy.orm import Session
from datetime import date
from sqlalchemy import func
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

def get_kid_activity_by_date(db: Session, kid_id: int, date_created: date):
    return db.query(models.CatatanMKids).filter(models.CatatanMKids.kid_id == kid_id, models.CatatanMKids.date_created == date_created).first()

def create_activity(db: Session, activity: schemas.CatatanMKidsCreate, kid_id: int):
    db_activity = models.CatatanMKids(**activity.dict(), kid_id=kid_id)
    db.add(db_activity)
    db.commit()
    db.refresh(db_activity)
    return db_activity

def update_activity(db: Session, activity_id: int, activity: schemas.CatatanMKidsCreate):
    db_activity = db.query(models.CatatanMKids).filter(models.CatatanMKids.id == activity_id).first()
    if db_activity:
        for key, value in activity.dict().items():
            setattr(db_activity, key, value)
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

from sqlalchemy.orm import Session
from sqlalchemy import func
from . import models, schemas
from datetime import date

def get_leaderboard(db: Session, start_date: date, end_date: date):
    leaderboard = (
        db.query(
            models.MuhajirinKids.id,
            models.MuhajirinKids.nama_lengkap,
            models.MuhajirinKids.nama_panggilan,
            func.sum(models.CatatanMKids.aktivitas_kedatangan).label("total_kedatangan"),
            func.sum(models.CatatanMKids.aktivitas_iqomat).label("total_iqomat"),
            func.sum(models.CatatanMKids.aktivitas_wudhu).label("total_wudhu"),
            func.sum(models.CatatanMKids.aktivitas_shof).label("total_shof"),
            func.sum(models.CatatanMKids.aktivitas_dzikir).label("total_dzikir"),
            func.sum(models.CatatanMKids.aktivitas_takkhusyusholat).label("total_takkhusyusholat"),
            func.sum(models.CatatanMKids.aktivitas_takkhusyukajian).label("total_takkhusyukajian"),
            func.sum(models.CatatanMKids.aktivitas_nyampah).label("total_nyampah"),
            func.sum(models.CatatanMKids.aktivitas_akhlakburuk).label("total_akhlakburuk"),
            (
                func.sum(models.CatatanMKids.aktivitas_kedatangan) +
                func.sum(models.CatatanMKids.aktivitas_iqomat) +
                func.sum(models.CatatanMKids.aktivitas_wudhu) +
                func.sum(models.CatatanMKids.aktivitas_shof) +
                func.sum(models.CatatanMKids.aktivitas_dzikir) -
                (
                    func.sum(models.CatatanMKids.aktivitas_takkhusyusholat) +
                    func.sum(models.CatatanMKids.aktivitas_takkhusyukajian) +
                    func.sum(models.CatatanMKids.aktivitas_nyampah) +
                    func.sum(models.CatatanMKids.aktivitas_akhlakburuk)
                )
            ).label("total_score")
        )
        .join(models.CatatanMKids, models.MuhajirinKids.id == models.CatatanMKids.kid_id)
        .filter(models.CatatanMKids.date_created.between(start_date, end_date))
        .group_by(models.MuhajirinKids.id)
        .order_by(
            (
                func.sum(models.CatatanMKids.aktivitas_kedatangan) +
                func.sum(models.CatatanMKids.aktivitas_iqomat) +
                func.sum(models.CatatanMKids.aktivitas_wudhu) +
                func.sum(models.CatatanMKids.aktivitas_shof) +
                func.sum(models.CatatanMKids.aktivitas_dzikir) -
                (
                    func.sum(models.CatatanMKids.aktivitas_takkhusyusholat) +
                    func.sum(models.CatatanMKids.aktivitas_takkhusyukajian) +
                    func.sum(models.CatatanMKids.aktivitas_nyampah) +
                    func.sum(models.CatatanMKids.aktivitas_akhlakburuk)
                )
            ).desc()
        )
    ).all()

    return leaderboard

def get_daily_leaderboard(db: Session, date: date):
    activities = db.query(models.CatatanMKids).filter(models.CatatanMKids.date_created == date).all()

    leaderboard = []
    for activity in activities:
        student = db.query(models.MuhajirinKids).filter(models.MuhajirinKids.id == activity.kid_id).first()
        positive_score = (activity.aktivitas_kedatangan + activity.aktivitas_iqomat + 
                          activity.aktivitas_wudhu + activity.aktivitas_shof + activity.aktivitas_dzikir)
        negative_score = (activity.aktivitas_takkhusyusholat + activity.aktivitas_takkhusyukajian + 
                          activity.aktivitas_nyampah + activity.aktivitas_akhlakburuk)

        total_score = positive_score - negative_score

        leaderboard.append({
            "id": student.id,
            "nama_panggilan": student.nama_panggilan,
            "positive_score": positive_score,
            "negative_score": negative_score,
            "total_score": total_score
        })

    # Sort leaderboard by total score in descending order
    leaderboard.sort(key=lambda x: x["total_score"], reverse=True)

    return leaderboard