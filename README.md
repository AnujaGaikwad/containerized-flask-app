Containerized Flask API on AWS ECS

A simple Flask REST API containerized with Docker, stored in Amazon ECR, and deployed on Amazon ECS using AWS Fargate. Amazon CloudWatch Logs is used for application monitoring.

Project Overview

This project demonstrates a complete container deployment workflow:

Flask API → Docker → Amazon ECR → Amazon ECS Fargate → CloudWatch Logs

The API provides three endpoints:

\- / — Returns the application status message

\- /health — Health endpoint

\- /api/info — Returns application and environment information

AWS Services Used

\- Amazon ECR — Stores the Docker container image

\- Amazon ECS — Runs and manages the container

\- AWS Fargate — Provides serverless container compute

\- Amazon CloudWatch Logs — Collects application logs

\- IAM — Provides the ECS task execution role

Project Structure

containerized-flask-app/

├── architecture/

├── screenshots/

├── .dockerignore

├── .gitignore

├── app.py

├── Dockerfile

├── requirements.txt

└── README.md

API Endpoints

Endpoint	Purpose

/	Application status

/health	Health check

/api/info	Application information





Docker Setup

Build the Docker image:

docker build -t cloudops-flask-api .

Run the container locally:

docker run -d -p 5002:5000 --name cloudops-flask-api cloudops-flask-api

The API is then available at:

http://localhost:5002/

http://localhost:5002/health

http://localhost:5002/api/info

Amazon ECR Deployment

The Docker image is tagged with the ECR repository URI and pushed to Amazon ECR.

docker tag cloudops-flask-api:latest <ECR-REPOSITORY-URI>:latest

docker push <ECR-REPOSITORY-URI>:latest

Amazon ECS Deployment

The application is deployed using:

\- ECS Cluster: cloudops-flask-cluster

\- ECS Service: cloudops-flask-service

\- Task Definition: cloudops-flask-task

\- Launch Type: Fargate

\- Container Port: 5000

\- CPU: 0.25 vCPU

\- Memory: 0.5 GiB

The ECS service runs one task using the Docker image stored in Amazon ECR.

CloudWatch Logging

Application logs are sent to the CloudWatch log group:

/cloudops/flask-api

The logs confirm that the Flask application starts successfully and that the API endpoints return successful HTTP responses.

Screenshots

Project evidence is available in the screenshots/ directory, including:

\- Local Flask application

\- Docker container

\- Docker health/API testing

\- ECR image push

\- ECR repository image

\- ECS cluster

\- CloudWatch log group

\- Live ECS API

\- CloudWatch application logs

Interview Explanation

I developed a Flask REST API, containerized it using Docker, pushed the Docker image to Amazon ECR, and deployed the container on Amazon ECS using Fargate. I configured CloudWatch Logs for monitoring and exposed health and API endpoints for testing.



One-line Architecture

Flask → Docker → ECR → ECS Fargate → CloudWatch

Future Improvements

\- Use Gunicorn instead of Flask's development server

\- Add an Application Load Balancer

\- Add HTTPS using AWS Certificate Manager

\- Add CI/CD using AWS CodePipeline and CodeBuild

\- Deploy the application in private subnets with production-grade networking

