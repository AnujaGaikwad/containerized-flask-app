# 🚀 Containerized Flask API on AWS ECS

A production-style container deployment project that demonstrates how to package a Python Flask REST API with Docker, store the container image in Amazon ECR, and deploy it on Amazon ECS using AWS Fargate, with application logs collected in Amazon CloudWatch.

## 🎯 Project Overview

This project demonstrates an end-to-end container deployment workflow:

**Flask API → Docker → Amazon ECR → Amazon ECS Fargate → CloudWatch Logs**

The application exposes three lightweight REST endpoints for application status, health monitoring, and environment information.

### API Endpoints

| Endpoint | Purpose |
|---|---|
| `/` | Returns application status |
| `/health` | Returns API health status |
| `/api/info` | Returns application and environment information |

---

## ☁️ AWS Services Used

| AWS Service | Purpose |
|---|---|
| **Amazon ECR** | Stores and manages the Docker container image |
| **Amazon ECS** | Runs and manages the containerized application |
| **AWS Fargate** | Provides serverless compute for the ECS task |
| **Amazon CloudWatch Logs** | Collects and monitors application logs |
| **AWS IAM** | Provides the ECS task execution role |

---

## 📁 Project Structure

```text
containerized-flask-app/
│
├── architecture/
│   └── mermaid-diagram.png
│
├── screenshots/
│   ├── 01-flask-local.png
│   ├── 03-docker-container.png
│   ├── 04-docker-health.png
│   ├── 05-ecr-push.png
│   ├── 06-ecr-image.png
│   ├── 07-ecs-cluster.png
│   ├── 09-cloudwatch-log-group.png
│   ├── 11-ecs-live-api.png
│   └── 12-cloudwatch-logs.png
│
├── .dockerignore
├── .gitignore
├── app.py
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## 🐍 Application

The API is built with **Python and Flask** and runs on port `5000` inside the container.

The application uses an environment variable named `APP_ENV` to demonstrate environment-specific configuration.

Default production configuration:

```text
APP_ENV=production
```

---

## 🐳 Docker

### Build the Docker Image

```bash
docker build -t cloudops-flask-api .
```

### Run Locally

```bash
docker run -d -p 5002:5000 --name cloudops-flask-api cloudops-flask-api
```

The host uses port `5002` because port `5000` was already being used by another local application.

### Test the API

```text
http://localhost:5002/
http://localhost:5002/health
http://localhost:5002/api/info
```

---

## 📦 Amazon ECR

The Docker image is stored in a private Amazon ECR repository.

### ECR Repository

```text
cloudops-flask-api
```

### Image URI

```text
669828370396.dkr.ecr.ap-south-1.amazonaws.com/cloudops-flask-api
```

### Tag the Image

```bash
docker tag cloudops-flask-api:latest 669828370396.dkr.ecr.ap-south-1.amazonaws.com/cloudops-flask-api:latest
```

### Push the Image

```bash
docker push 669828370396.dkr.ecr.ap-south-1.amazonaws.com/cloudops-flask-api:latest
```

---

## 🚀 Amazon ECS Fargate Deployment

The container was deployed to Amazon ECS using AWS Fargate.

### ECS Configuration

| Configuration | Value |
|---|---|
| **Cluster** | `cloudops-flask-cluster` |
| **Service** | `cloudops-flask-service` |
| **Task Definition** | `cloudops-flask-task` |
| **Launch Type** | Fargate |
| **Container Port** | `5000` |
| **CPU** | `0.25 vCPU` |
| **Memory** | `0.5 GiB` |
| **Platform** | Linux / X86_64 |
| **Network Mode** | `awsvpc` |

The ECS task pulls the Docker image from Amazon ECR and runs the Flask API as a Fargate task.

---

## 📊 CloudWatch Logging

Application logs are sent to:

```text
/cloudops/flask-api
```

CloudWatch captured:

- Flask application startup
- Incoming API requests
- HTTP response status codes
- Application runtime information

Example successful requests included:

```text
GET / HTTP/1.1 → 200
GET /health HTTP/1.1 → 200
GET /api/info HTTP/1.1 → 200
```

This confirms that the deployed application was receiving requests successfully and that ECS-to-CloudWatch logging was working.

---

## 🖼️ Screenshots

The `screenshots/` directory contains project evidence covering:

1. Local Flask application
2. Docker container
3. Docker API/health testing
4. ECR image push
5. ECR repository image
6. ECS cluster
7. CloudWatch log group
8. Live ECS API
9. CloudWatch application logs

---

## 🏗️ Architecture

The project architecture is available separately in:



### Workflow

```text
Developer
   ↓
Flask REST API
   ↓
Docker Image
   ↓
Amazon ECR
   ↓
Amazon ECS Fargate
   ↓
CloudWatch Logs
```

---

## 🎤 Interview Explanation

> I developed a Flask REST API and containerized it using Docker. I pushed the Docker image to Amazon ECR and deployed it on Amazon ECS using Fargate. I configured CloudWatch Logs for application monitoring and tested the deployed API using health and information endpoints.

### One-Line Explanation

**Flask → Docker → ECR → ECS Fargate → CloudWatch**

---

## 🔮 Future Improvements

- Replace Flask's development server with **Gunicorn**
- Add an **Application Load Balancer**
- Enable **HTTPS** using AWS Certificate Manager
- Implement **CI/CD** using AWS CodePipeline and CodeBuild
- Deploy using **private subnets** and production-grade networking
- Add ECS container health checks
- Add automated deployment and monitoring

---

## 📚 Key Learnings

- Building REST APIs with Flask
- Creating optimized Docker images
- Running containers locally
- Publishing images to Amazon ECR
- Deploying containers using Amazon ECS Fargate
- Configuring ECS task execution roles
- Configuring CloudWatch container logging
- Testing and monitoring a deployed containerized application
- Managing AWS resources and cleaning up cost-incurring resources

---

## 👩‍💻 Author

**Anuja Gaikwad**


GitHub: [AnujaGaikwad](https://github.com/AnujaGaikwad)
