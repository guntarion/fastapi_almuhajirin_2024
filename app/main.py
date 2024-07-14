from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import init_db
from .app_klinik.routers import router as clinic_router
from .app_masjid.routers import router as masjid_router

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to specify allowed origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

init_db()

# Include the clinic router
app.include_router(clinic_router, prefix="/clinic", tags=["clinic"])
app.include_router(masjid_router, prefix="/masjid", tags=["masjid"])


@app.get("/")
async def read_root():
    return {"message": "Server is running okay"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)