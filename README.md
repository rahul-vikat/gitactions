# GitHub Actions CI/CD Tutorial

This repository demonstrates a comprehensive GitHub Actions CI/CD pipeline as featured in the tutorial video.

## Core Concepts

- **Git vs GitHub**: Git is a version control system; GitHub is the code repository platform
- **Continuous Integration (CI)**: Automating builds and tests upon code commits to prevent integration errors
- **Continuous Deployment (CD)**: Automated movement of code through testing environments to production

## Developer Workflow

1. Create feature branches
2. Perform manual code reviews via pull requests
3. Trigger automated pipelines for testing

## CI/CD Pipeline

This project includes a GitHub Actions workflow that automatically runs pytest unit tests whenever code is pushed or a pull request is created.

### Workflow File

`.github/workflows/ci.yml` - Triggers on `push` and `pull_request` events, runs pytest in a Ubuntu environment.

### Local Development

1. Install dependencies: `python -m pip install pytest`
2. Run tests: `pytest`
3. All tests are defined in `test_app.py`

### Project Structure

```
gitactions/
├── app.py              # Simple Python module with arithmetic functions
├── test_app.py         # pytest unit tests for app functions
├── .github/
│   └── workflows/
│       └── ci.yml      # GitHub Actions CI/CD configuration
└── README.md           # This file