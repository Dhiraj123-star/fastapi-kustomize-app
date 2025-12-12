
## 🚀 FastAPI + Docker + Kustomize Starter

A **minimal, production-ready FastAPI starter** containerized with Docker, built and published via **GitHub Actions**, and deployed on Kubernetes using **Kustomize**.
Designed to work smoothly with **Minikube** and scale later.

-----

## ✨ Features

  * ✅ Minimal FastAPI application
  * ✅ Dockerized with production-ready Dockerfile
  * ✅ Automated Docker image build & push via GitHub Actions
  * ✅ Kubernetes manifests managed with Kustomize
  * ✅ Environment-specific overlays (dev)
  * ✅ Works with Minikube (no local Docker hacks)
  * **✨ Ingress-based external routing (`fastapi.dev.local`)**
  * **🔒 Self-signed TLS/SSL enabled for local HTTPS access**
  * **🔑 SAN-compliant certificate generation for modern NGINX Ingress Controllers**

## 📂 Project Structure

```
app/
  └── main.py
k8s/
  ├── base/
  │   ├── deployment.yaml
  │   ├── service.yaml
  │   ├── ingress.yaml        # Added Ingress resource
  │   └── kustomization.yaml
  └── overlays/
      └── dev/
          ├── kustomization.yaml
          ├── patch-deployment.yaml
          └── patch-ingress-tls.yaml  # Added TLS patch
.github/
  └── workflows/
      └── docker-publish.yml
Dockerfile
requirements.txt
README.md
openssl.cnf                     # Added for SAN certificate generation
tls.key (Ignored by Git)
tls.crt (Ignored by Git)
```

-----

## 🛠️ Run Locally (Without Docker)

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Visit:
👉 [http://localhost:8000](https://www.google.com/search?q=http://localhost:8000)

-----

## 🐳 Docker Image (CI/CD Managed)

Docker image is **automatically built and pushed** to Docker Hub on every push to `main`.

```
dhiraj918106/fastapi-kustomize:latest
```

No manual Docker build or push required.

-----

## ☸️ Deploy to Kubernetes (Minikube)

### 1️⃣ Prepare Environment and Certificate (First Run)

To enable HTTPS, you must generate a SAN-compliant certificate and patch the NGINX Service.

1.  **Start Minikube and Ingress:**
    ```bash
    minikube start
    minikube addons enable ingress
    ```
2.  **Generate Certificate:** Use the provided `openssl.cnf` to create the key and certificate.
    ```bash
    openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout tls.key -out tls.crt -config openssl.cnf
    ```
3.  **Create Kubernetes Secret:**
    ```bash
    kubectl create secret tls fastapi-tls-secret --key tls.key --cert tls.crt
    ```

-----

### 2️⃣ Deploy using Kustomize

Apply the configuration, which includes the Ingress resource and the TLS patch for the dev overlay.

```bash
kubectl apply -k k8s/overlays/dev
```

**Patch NGINX Service:** Convert the default NGINX service to a `LoadBalancer` for easier access on standard ports (443).

```bash
kubectl patch service ingress-nginx-controller -n ingress-nginx -p '{"spec": {"type": "LoadBalancer"}}'
```

-----

### 3️⃣ Access the Application (HTTPS)

1.  **Start Minikube Tunnel:** Run this command in a **separate, dedicated terminal** and **leave it running**. This exposes the LoadBalancer IP to your host.

    ```bash
    minikube tunnel
    ```

2.  **Update `/etc/hosts`:** Get your Minikube IP (`minikube ip`) and map the hostname in your local hosts file (`/etc/hosts`).

    ```bash
    # Use your Minikube IP address here
    # Example: 192.168.58.2    fastapi.dev.local
    ```

3.  **Test HTTPS Access:** Use `curl -k` (for insecure/self-signed cert) or visit the URL in your browser after accepting the security warning.

    ```bash
    curl -k https://fastapi.dev.local
    ```

    Visit:
    👉 [https://fastapi.dev.local](https://www.google.com/search?q=https://fastapi.dev.local)

-----
