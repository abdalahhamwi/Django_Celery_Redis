# Django_Celery_Redis

A production‑ready Django project demonstrating asynchronous task processing using **Celery** with **Redis** as both the broker and result backend.  
This setup is ideal for handling background jobs such as sending emails, scheduled tasks, heavy computations, and real‑time processing.



## 🚀 Features
- Django backend with clean project structure  
- Celery integration for asynchronous tasks  
- Redis as message broker & result backend  
- Example task (`sending`)  
- Docker‑ready structure (optional)  
- Easy to deploy on Render, DigitalOcean, or any VPS  



## 📦 Requirements
- Python 3.12+  
- Django 5+  
- Redis Server  
- Celery 5+  



# 🐳 Run the Project with Docker

## 1️⃣ Build & start all services
```bash
docker-compose up --build
