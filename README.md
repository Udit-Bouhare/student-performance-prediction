# Student Performance Prediction 🚀

An end-to-end **Machine Learning web application** that predicts student performance based on input features.  
The project is fully **containerized** and deployed using a **complete CI/CD pipeline**.

---

## 🌐 Live Application

👉 **Live URL:** https://student-performance-prediction-s6i1.onrender.com

---

## 🔧 Tech Stack

- Python
- Flask
- Scikit-learn
- CatBoost / XGBoost
- Docker
- GitHub Actions (CI/CD)
- GitHub Container Registry (GHCR)
- Render (Deployment)

---

## 📌 Project Features

- Machine Learning model for student performance prediction
- Flask-based web application
- REST API endpoint for predictions
- Dockerized application using Gunicorn
- Automated testing using `pytest`
- Fully automated CI pipeline
- Docker image automatically built & pushed to GHCR
- Automatic deployment on Render after successful CI

---

## ⚙️ CI/CD Workflow

This project follows a **production-style CI/CD pipeline**:

1. Code is pushed to the `main` branch
2. GitHub Actions workflow is triggered
3. Dependencies are installed
4. Tests are executed using `pytest`
5. Docker image is built
6. Image is pushed to **GitHub Container Registry (GHCR)**
7. Render pulls the latest image and deploys it automatically

✅ If tests fail → deployment is blocked  
✅ If tests pass → deployment happens automatically

---

## 🐳 Docker

- Application is containerized using Docker
- Gunicorn is used as the production server
- Docker images are stored in GHCR

## 🧪 Testing

- Unit tests written using `pytest`
- Tests are mandatory in CI
- Deployment happens only after tests pass

---

## 🚀 Deployment

- Deployed on **Render**
- Uses Docker image from **GitHub Container Registry**
- No manual deployment steps

---

## 📌 Notes

This project demonstrates **real-world ML deployment practices**, including CI/CD, Dockerization, automated testing, and cloud deployment.