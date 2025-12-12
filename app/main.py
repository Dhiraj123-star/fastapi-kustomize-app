from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message":"Hello from FastAPI + Docker + Kustomize + Github Actions!!"}

@app.get("/healthz")
def health_check():
    """
    Kubernetes Readiness and Liveness Probe endpoint.
    Returns 200 OK if the application is running.
    """
    return {"status":"Ok"}
