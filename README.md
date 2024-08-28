# bbtlab-app01-ci-dc with CI/CD Pipeline
Simple Python Flask web application that is containerized using Docker and deployed using a Continuous Integration/Continuous Deployment (CI/CD) pipeline.

## Overview

This project is a simple Flask web application designed to demonstrate the integration of Continuous Integration (CI) and Continuous Deployment (CD) using tools like GitHub Actions and Docker. The application is automatically tested and deployed using a CI/CD pipeline.

## Features

- Simple Flask web application
- Automated testing with `unittest`
- Dockerized environment
- Continuous Integration and Deployment using GitHub Actions
- Deployed to a Docker container

## Project Structure
```
bbtlab-app01-ci-cd/
├── .github/
│   └── workflows/
│       └── ci-cd.yml
├── app/
│   ├── app.py
│   ├── templates/
│   │   ├── index.html
│   │   ├── about.html
│   │   └── contact.html
│   └── static/
│       └── style.css
├── tests/
│   ├── test_app.py
├── Dockerfile
├── docker-compose.yml
├── Jenkinsfile
├── requirements.txt
├── README.md
└── .gitignore

```

## Getting Started

### Prerequisites

Ensure you have the following installed on your local machine:

- Python 3.12
- Docker
- Git

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/BBTHomeLab/bbtlab-app01-ci-dc.git
   cd bbtlab-app01-ci-dc
   ```
2. **Create a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application locally:**
   ```bash
   python app/app.py
   ```
The application should now be running at http://127.0.0.1:5000.
