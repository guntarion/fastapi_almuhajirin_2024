from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from . import crud, schemas
from ..database import get_clinic_db

router = APIRouter()

@router.post("/patients/", response_model=schemas.Patient)
def create_patient(patient: schemas.PatientCreate, db: Session = Depends(get_clinic_db)):
    db_patient = crud.get_patient_by_reg_id(db, reg_id=patient.reg_id)
    if db_patient:
        raise HTTPException(status_code=400, detail="Patient already registered")
    return crud.create_patient(db=db, patient=patient)

@router.get("/patients/", response_model=List[schemas.Patient])
def read_patients(skip: int = 0, limit: int = 100, db: Session = Depends(get_clinic_db)):
    patients = crud.get_patients(db, skip=skip, limit=limit)
    return patients

@router.put("/patients/{patient_id}", response_model=schemas.Patient)
def update_patient(patient_id: int, patient: schemas.PatientCreate, db: Session = Depends(get_clinic_db)):
    db_patient = crud.update_patient(db, patient_id, patient)
    if db_patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    return db_patient

@router.delete("/patients/{patient_id}", response_model=schemas.Patient)
def delete_patient(patient_id: int, db: Session = Depends(get_clinic_db)):
    db_patient = crud.delete_patient(db, patient_id)
    if db_patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    return db_patient

@router.get("/appointments/", response_model=List[schemas.Appointment])
def read_appointments(skip: int = 0, limit: int = 100, db: Session = Depends(get_clinic_db)):
    appointments = crud.get_appointments(db, skip=skip, limit=limit)
    return appointments

@router.post("/appointments/", response_model=schemas.Appointment)
def create_appointment(appointment: schemas.AppointmentCreate, db: Session = Depends(get_clinic_db)):
    return crud.create_appointment(db=db, appointment=appointment)

@router.put("/appointments/{appointment_id}", response_model=schemas.Appointment)
def update_appointment(appointment_id: int, appointment: schemas.AppointmentCreate, db: Session = Depends(get_clinic_db)):
    db_appointment = crud.update_appointment(db, appointment_id, appointment)
    if db_appointment is None:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return db_appointment

@router.delete("/appointments/{appointment_id}", response_model=schemas.Appointment)
def delete_appointment(appointment_id: int, db: Session = Depends(get_clinic_db)):
    db_appointment = crud.delete_appointment(db, appointment_id)
    if db_appointment is None:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return db_appointment

@router.get("/treatments/", response_model=List[schemas.Treatment])
def read_treatments(skip: int = 0, limit: int = 100, db: Session = Depends(get_clinic_db)):
    treatments = crud.get_treatments(db, skip=skip, limit=limit)
    return treatments

@router.post("/treatments/", response_model=schemas.Treatment)
def create_treatment(treatment: schemas.TreatmentCreate, db: Session = Depends(get_clinic_db)):
    return crud.create_treatment(db=db, treatment=treatment)

@router.get("/medications/", response_model=List[schemas.Medication])
def read_medications(skip: int = 0, limit: int = 100, db: Session = Depends(get_clinic_db)):
    medications = crud.get_medications(db, skip=skip, limit=limit)
    return medications

@router.post("/medications/", response_model=schemas.Medication)
def create_medication(medication: schemas.MedicationCreate, db: Session = Depends(get_clinic_db)):
    return crud.create_medication(db=db, medication=medication)

@router.get("/staff/", response_model=List[schemas.Staff])
def read_staff(skip: int = 0, limit: int = 100, db: Session = Depends(get_clinic_db)):
    staff = crud.get_staffs(db, skip=skip, limit=limit)
    return staff

@router.post("/staff/", response_model=schemas.Staff)
def create_staff(staff: schemas.StaffCreate, db: Session = Depends(get_clinic_db)):
    return crud.create_staff(db=db, staff=staff)

@router.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_clinic_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users

@router.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_clinic_db)):
    return crud.create_user(db=db, user=user)

@router.get("/checkups/", response_model=List[schemas.Checkup])
def read_checkups(skip: int = 0, limit: int = 100, db: Session = Depends(get_clinic_db)):
    checkups = crud.get_checkups(db, skip=skip, limit=limit)
    return checkups

@router.post("/checkups/", response_model=schemas.Checkup)
def create_checkup(checkup: schemas.CheckupCreate, db: Session = Depends(get_clinic_db)):
    return crud.create_checkup(db=db, checkup=checkup)