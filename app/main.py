from fastapi import FastAPI
import os
from .database import initialize_db, check_db_connection

WELCOME_MESSAGE = os.getenv("WELCOME_MESSAGE","ConfigMap variable not set. Fallback!!")
DB_PATH = os.getenv("SQLITE_DATABASE_PATH", "DB path not set. Fallback!!") 

app = FastAPI()

@app.on_event("startup")
def startup_event():
    success=initialize_db()
    if not success:
        print("Database failed to initialize. Proceeding with limited functionality.")


@app.get("/")
def read_root():
    return {"message":"Hello from FastAPI + Docker + Kustomize + Github Actions!!"}

@app.get("/config-message")
def get_config_message():
    return {"message":WELCOME_MESSAGE}

@app.get("/healthz")
def health_check():
    """
    Check application and database health
    """
    db_ok,db_message= check_db_connection()

    if db_ok:
        return {"status":"Ok", "db_status":db_message}

    else:
        return {"status":"Degraded","db_status":db_message},503

    
