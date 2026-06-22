# DevOps Address Validation Application

## 📌 Project Overview

This project demonstrates the end-to-end deployment of a containerised web application backed by a PostgreSQL database using Docker and Kubernetes.

The application queries a PostgreSQL database containing sample address records and dynamically generates an HTML report that is served to users through Nginx. The project was initially developed using standalone Docker containers before being migrated to a local Kubernetes cluster created with **kind (Kubernetes in Docker)**.

Throughout the project, modern Platform Engineering practices were implemented, including the use of Deployments, Services, ConfigMaps, Secrets, PersistentVolumeClaims (PVCs), readiness probes, and liveness probes.

---

# 🏗️ Architecture

```
                           Browser
                              │
                              ▼
                   kubectl port-forward
                              │
                              ▼
                     web-service (ClusterIP)
                              │
                              ▼
                     Web Deployment / Pod
                              │
                              ▼
                 postgres-service (ClusterIP)
                              │
                              ▼
                 PostgreSQL Deployment / Pod
                              │
                              ▼
               PersistentVolumeClaim (PVC)
                              │
                              ▼
                   Persistent Kubernetes Storage
```

---

# 📁 Project Structure

```
devops-address-test/

├── database/
│   ├── Dockerfile
│   └── init.sql
│
├── web/
│   ├── Dockerfile
│   ├── app.py
│   └── entrypoint.sh
│
├── k8s/
│   ├── postgres-configmap.yaml
│   ├── postgres-secret.yaml
│   ├── postgres-pvc.yaml
│   ├── postgres-deployment.yaml
│   ├── postgres-service.yaml
│   ├── web-deployment.yaml
│   └── web-service.yaml
│
├── kind-cluster.yaml
└── README.md
```

---

# 🚀 Technologies Used

* Ubuntu Linux
* Docker
* Docker Networking
* PostgreSQL 16
* Python 3.10
* Nginx
* Kubernetes
* kind (Kubernetes in Docker)
* kubectl
* Git
* GitHub

---

# 🐳 Docker Implementation

A custom PostgreSQL Docker image was built from the official `postgres:16` image. During the build process, an `init.sql` script is copied into the image so that the database schema and seed data are automatically created when the container starts.

The web application was built as a separate Docker image using Python and Nginx. A Python script queries the PostgreSQL database and generates an HTML report which is then served by Nginx.

Separating the database and web application into individual containers follows containerisation best practices by ensuring each container has a single responsibility.

---

# ☸️ Kubernetes Implementation

The application was migrated from standalone Docker containers into a local Kubernetes cluster using **kind**.

The deployment consists of:

* PostgreSQL Deployment
* PostgreSQL Service
* Web Deployment
* Web Service
* ConfigMap
* Secret
* PersistentVolumeClaim

The Services provide stable DNS names and virtual IP addresses, allowing Pods to communicate reliably even if individual Pods are recreated.

---

# 🔐 Configuration Management

## ConfigMap

The ConfigMap stores non-sensitive configuration values such as:

* Database name
* Database username

This separates configuration from application code.

## Secret

Sensitive information such as the PostgreSQL password is stored inside a Kubernetes Secret instead of being hardcoded into the application or deployment manifests.

---

# 💾 Persistent Storage

A PersistentVolumeClaim (PVC) is used to ensure that PostgreSQL data survives Pod recreation.

Without persistent storage, deleting the Pod would also remove the database files stored inside the container filesystem.

By mounting the PVC to:

```
/var/lib/postgresql/data
```

the database remains available even after Kubernetes recreates the Pod.

---

# ❤️ Health Checks

The project implements both readiness and liveness probes.

### Readiness Probe

Uses:

```
pg_isready
```

to determine when PostgreSQL is ready to accept client connections.

### Liveness Probe

Monitors the running PostgreSQL instance and allows Kubernetes to automatically restart the container if it becomes unhealthy.

The web deployment also exposes HTTP health checks to verify that Nginx is successfully serving content.

---

# 🧪 Validation

The project was validated by:

* Successfully deploying both applications to Kubernetes.
* Accessing the generated HTML report through a browser.
* Connecting to PostgreSQL using `psql`.
* Executing:

```sql
SELECT * FROM addresses;
```

* Confirming all seeded address records were present.

---

# 🔧 Troubleshooting Experience

During development several real-world issues were encountered and resolved, including:

* Docker socket permission errors.
* PostgreSQL startup failures caused by incorrect environment variable names.
* Docker container naming conflicts.
* Nginx serving the default welcome page instead of generated content.
* Loading custom Docker images into a kind cluster.
* Installing and configuring `kubectl`.
* Configuring `kubectl port-forward` to bind to `0.0.0.0` instead of `127.0.0.1` for external browser access.
* Installing the PostgreSQL client (`psql`) for database validation.
* Implementing persistent storage using a PersistentVolumeClaim.

Each issue was investigated, diagnosed, and resolved using a structured troubleshooting approach.

---

# 📚 Key Learning Outcomes

This project strengthened practical experience in:

* Linux administration
* Docker image creation
* Container networking
* PostgreSQL administration
* Python application development
* Nginx configuration
* Kubernetes Deployments
* Kubernetes Services
* ConfigMaps and Secrets
* Persistent storage using PVCs
* Readiness and liveness probes
* Git and GitHub workflows
* Systematic troubleshooting and debugging

---

# 🎯 Future Improvements

Potential future enhancements include:

* Ingress controller implementation.
* Automatic TLS using cert-manager.
* CI/CD pipeline using GitHub Actions or Jenkins.
* Helm chart packaging.
* Horizontal Pod Autoscaler (HPA).
* Monitoring with Prometheus and Grafana.
* Centralised logging using the ELK stack.
* Deployment to a managed Kubernetes platform such as Google Kubernetes Engine (GKE).
