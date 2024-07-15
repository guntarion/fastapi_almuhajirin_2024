from typing import List, Optional
from pydantic import BaseModel
from datetime import date
from typing import List, Optional

class CatatanMKidsBase(BaseModel):
    aktivitas_kedatangan: int
    aktivitas_iqomat: int
    aktivitas_wudhu: int
    aktivitas_shof: int
    aktivitas_dzikir: int
    aktivitas_takkhusyusholat: int
    aktivitas_takkhusyukajian: int
    aktivitas_nyampah: int
    aktivitas_akhlakburuk: int
    date_created: date
    recorder_name: str


class CatatanMKidsCreate(CatatanMKidsBase):
    pass


class CatatanMKids(CatatanMKidsBase):
    id: int
    kid_id: int

    class Config:
        orm_mode = True


class MuhajirinKidsBase(BaseModel):
    nama_lengkap: str
    nama_panggilan: str
    tanggal_lahir: Optional[date] = None
    gender: Optional[str] = None
    nomer_hp: Optional[str] = None
    email: Optional[str] = None
    alamat_jalan: Optional[str] = None
    alamat_rw: Optional[str] = None
    alamat_rt: Optional[str] = None
    alamat_domisili: Optional[str] = None


class MuhajirinKidsCreate(MuhajirinKidsBase):
    pass


class MuhajirinKids(MuhajirinKidsBase):
    id: int
    activities: List[CatatanMKids] = []

    class Config:
        orm_mode = True


class BadgeBase(BaseModel):
    badge_nama: str
    badge_keterangan: str
    badge_poinambang: float


class BadgeCreate(BadgeBase):
    pass


class Badge(BadgeBase):
    id: int

    class Config:
        orm_mode = True

from pydantic import BaseModel
from typing import List, Optional

class LeaderboardStudent(BaseModel):
    id: int
    nama_lengkap: str
    nama_panggilan: str
    total_kedatangan: Optional[int] = 0
    total_iqomat: Optional[int] = 0
    total_wudhu: Optional[int] = 0
    total_shof: Optional[int] = 0
    total_dzikir: Optional[int] = 0
    total_takkhusyusholat: Optional[int] = 0
    total_takkhusyukajian: Optional[int] = 0
    total_nyampah: Optional[int] = 0
    total_akhlakburuk: Optional[int] = 0
    total_score: int

    class Config:
        orm_mode = True
