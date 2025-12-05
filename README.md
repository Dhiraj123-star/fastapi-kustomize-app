
# 🚀 FastAPI + Docker + Kustomize Starter

A minimal FastAPI application packaged with Docker and deployed on Kubernetes using **Kustomize**.

---

## 📦 Features

- Simple FastAPI app  
- Dockerized application  
- Kubernetes manifests with Kustomize overlays  
- Ready for local KIND / Minikube deployment  

---

## 🛠️ Run Locally

### 1. Install dependencies

```bash
pip install -r requirements.txt
````

### 2. Start the server

```bash
uvicorn app.main:app --reload
```

Go to:
👉 [http://localhost:8000](http://localhost:8000)

---

## 🐳 Build & Run with Docker

```bash
docker build -t fastapi-kustomize .
docker run -p 8000:8000 fastapi-kustomize
```

---

## ☸ Deploy to Kubernetes with Kustomize

### Build manifest:

```bash
kustomize build k8s/overlays/dev
```

### Apply:

```bash
kubectl apply -k k8s/overlays/dev
```

---

## 📂 Project Structure

```
app/
k8s/
Dockerfile
requirements.txt
README.md
```

---

## ✅ Ready for Next Steps

We can later add:

* Ingress
* Autoscaling
* ConfigMaps & Secrets
* CI/CD
* Logging, Monitoring
* Multiple environments

---
