from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Database URLs
base_dir = os.path.dirname(os.path.abspath(__file__))
CLINIC_DATABASE_URL = f"sqlite:///{os.path.join(base_dir, 'app_klinik', 'clinic.db')}"
MASJID_DATABASE_URL = f"sqlite:///{os.path.join(base_dir, 'app_masjid', 'masjid.db')}"
KBTK_DATABASE_URL = f"sqlite:///{os.path.join(base_dir, 'app_kbtk', 'kbtk.db')}"

# Create engines
clinic_engine = create_engine(CLINIC_DATABASE_URL, connect_args={"check_same_thread": False})
masjid_engine = create_engine(MASJID_DATABASE_URL, connect_args={"check_same_thread": False})
kbtk_engine = create_engine(KBTK_DATABASE_URL, connect_args={"check_same_thread": False})

# Create session locals
ClinicSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=clinic_engine)
MasjidSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=masjid_engine)
KbtkSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=kbtk_engine)

# Base class for models
Base = declarative_base()

def get_clinic_db():
    db = ClinicSessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_masjid_db():
    db = MasjidSessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_kbtk_db():
    db = KbtkSessionLocal()
    try:
        yield db
    finally:
        db.close()

def init_db():
    from .app_klinik import models as clinic_models
    from .app_masjid import models as masjid_models
    from .app_kbtk import models as kbtk_models

    clinic_models.Base.metadata.create_all(bind=clinic_engine)
    masjid_models.Base.metadata.create_all(bind=masjid_engine)
    kbtk_models.Base.metadata.create_all(bind=kbtk_engine)