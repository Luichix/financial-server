from fastapi import FastAPI
from app.routers import amortizations, financial_statements, reports
from fastapi.middleware.cors import CORSMiddleware

from apscheduler.schedulers.background import BackgroundScheduler
from app.utils.remove_temporal import delete_temporary_files
import atexit

app = FastAPI()

# Include routes
app.include_router(amortizations.router)
app.include_router(financial_statements.router)
app.include_router(reports.router)

# Handle cors
origins = ["*"]

# Add middlewares
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Start background programming tasks
scheduler = BackgroundScheduler()
scheduler.add_job(delete_temporary_files, "interval", hours=24, args=["app/temp"])
scheduler.start()

# Detener el planificador cuando la aplicación se cierra
atexit.register(lambda: scheduler.shutdown())
