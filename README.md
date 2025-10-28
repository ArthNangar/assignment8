# 🚀 FastAPI Calculator — Module 8

### Overview  
This project is part of the **FastAPI Web Application Module**, focused on building, testing, and enhancing a calculator application using **FastAPI**, **Playwright**, and **GitHub Actions**.  
It demonstrates how a simple calculator can evolve into a fully tested web app with logging, CI, and modern development workflows.

---

## Features

**FastAPI Backend** – RESTful API endpoints for arithmetic operations  
**Frontend Integration** – HTML & JavaScript interface for user interaction  
**Comprehensive Testing** – Unit, Integration, and End-to-End tests  
**Logging** – Tracks operations, errors, and API activity  
**Continuous Integration** – Automated test runs via GitHub Actions  
**Version Control** – Organized commits following best Git practices  

---

## Project Structure
```

.assignment8/
├── .github/
│ └── workflows/
│ └── test.yml    ## GitHub Actions CI workflow
├── .vscode/
│ └── settings.json
├── app/
│ └── operations/
│ └── init.py
├── templates/
│ └── index.html    ## Frontend template
├── tests/
│ ├── unit/
│ │ ├── init.py
│ │ └── test_calculator.py   ## Unit tests for operations
│ ├── integration/
│ │ ├── init.py
│ │ └── test_fastapi_calculator.py  ## Integration tests for API
│ └── e2e/
│ ├── init.py
│ └── test_e2e.py    ## End-to-end tests (Playwright)
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── LICENSE
├── main.py      ## FastAPI application entry point
├── pytest.ini
├── requirements.txt
└── README.md

```

## Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/fastapi-calculator.git
cd assginment8

Create Virtual Environment
python -m venv venv
source venv/bin/activate  
On Windows: venv\Scripts\activate


Install Dependencies
pip install -r requirements.txt

Run the Application
python main.py
Then open your browser at 👉 http://127.0.0.1:8000


```

##  Running Tests
```
Unit & Integration Tests
pytest --cov=app tests/

End-to-End Tests (Playwright)
pytest tests/test_e2e_playwright.py

```

## Example Usage
```
Request:
GET /add?a=10&b=5

Response:
json
{
  "operation": "add",
  "a": 10,
  "b": 5,
  "result": 15
}
```

## CI/CD Pipeline

The GitHub Actions pipeline includes three stages:

1. **Test** - Executes all unit, integration, and end-to-end tests,  ensuring full coverage and stable functionality.
2. **Security** - Performs a vulnerability scan on the Docker image using Trivy, automatically failing the build if any critical or high-severity issues are detected.
3. **Deploy** - Builds and publishes multi-platform Docker images (for AMD64 and ARM64) to Docker Hub.

### Required GitHub Secrets
- `DOCKERHUB_USERNAME`
- `DOCKERHUB_TOKEN`

### Pipeline Features
- Automated test execution on every push and pull request
- Built-in container security scanning and quality gates
- Seamless, cross-platform image builds and deployment to Docker Hub

## Author
Arth Nangar

Date : 10/27/2025
