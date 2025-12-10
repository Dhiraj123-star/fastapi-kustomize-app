
# 🚀 FastAPI + Docker + Kustomize Starter

A **minimal, production-ready FastAPI starter** containerized with Docker, built and published via **GitHub Actions**, and deployed on Kubernetes using **Kustomize**.
Designed to work smoothly with **Minikube** and scale later.

---

## ✨ Features

* ✅ Minimal FastAPI application
* ✅ Dockerized with production-ready Dockerfile
* ✅ Automated Docker image build & push via GitHub Actions
* ✅ Kubernetes manifests managed with Kustomize
* ✅ Environment-specific overlays (dev)
* ✅ Works with Minikube (no local Docker hacks)

---

## 📦 Architecture Overview

```
GitHub Actions → Docker Hub → Kubernetes (Minikube)
```

---

## 📂 Project Structure

```
app/
  └── main.py
k8s/
  ├── base/
  │   ├── deployment.yaml
  │   ├── service.yaml
  │   └── kustomization.yaml
  └── overlays/
      └── dev/
          ├── kustomization.yaml
          └── patch-deployment.yaml
.github/
  └── workflows/
      └── docker-publish.yml
Dockerfile
requirements.txt
README.md
```

---

## 🛠️ Run Locally (Without Docker)

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Visit:
👉 [http://localhost:8000](http://localhost:8000)

---

## 🐳 Docker Image (CI/CD Managed)

Docker image is **automatically built and pushed** to Docker Hub on every push to `main`.

```
dhiraj918106/fastapi-kustomize:latest
```

No manual Docker build or push required.

---

## ☸️ Deploy to Kubernetes (Minikube)

### 1️⃣ Start Minikube

```bash
minikube start
```

(Optional but recommended)

```bash
minikube addons enable ingress
```

---

### 2️⃣ Deploy using Kustomize

```bash
kubectl apply -k k8s/overlays/dev
```

---

### 3️⃣ Verify Resources

```bash
kubectl get pods
kubectl get svc
```

---

### 4️⃣ Access the Application

```bash
minikube service fastapi-service
```

or

```bash
kubectl port-forward svc/fastapi-service 8000:8000
```

Visit:
👉 [http://localhost:8000](http://localhost:8000)

---