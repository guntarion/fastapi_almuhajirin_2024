from sqlalchemy import Column, Integer, String, Float, Date, Boolean, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from ..database import Base  # Import Base from the central database file


class MuhajirinKids(Base):
    __tablename__ = "muhajirin_kids"

    id = Column(Integer, primary_key=True, index=True)
    nama_lengkap = Column(String, index=True)
    nama_panggilan = Column(String, index=True)
    tanggal_lahir = Column(Date, nullable=True)
    gender = Column(String, nullable=True)
    nomer_hp = Column(String, nullable=True)
    email = Column(String, nullable=True)
    alamat_jalan = Column(String, nullable=True)
    alamat_rw = Column(String, nullable=True)
    alamat_rt = Column(String, nullable=True)
    alamat_domisili = Column(String, nullable=True)

    activities = relationship("CatatanMKids", back_populates="kid")


class CatatanMKids(Base):
    __tablename__ = "catatan_mkids"

    id = Column(Integer, primary_key=True, index=True)
    aktivitas_kedatangan = Column(Integer)
    aktivitas_iqomat = Column(Integer)
    aktivitas_wudhu = Column(Integer)
    aktivitas_shof = Column(Integer)
    aktivitas_dzikir = Column(Integer)
    aktivitas_takkhusyusholat = Column(Integer)
    aktivitas_takkhusyukajian = Column(Integer)
    aktivitas_nyampah = Column(Integer)
    aktivitas_akhlakburuk = Column(Integer)
    date_created = Column(Date)
    recorder_name = Column(String)  # Add recorder_name field

    kid_id = Column(Integer, ForeignKey('muhajirin_kids.id'))
    kid = relationship("MuhajirinKids", back_populates="activities")


class Badge(Base):
    __tablename__ = "badges"

    id = Column(Integer, primary_key=True, index=True)
    badge_nama = Column(String)
    badge_keterangan = Column(String)
    badge_poinambang = Column(Float)
