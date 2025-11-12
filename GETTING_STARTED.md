# Getting Started with py_wise Advanced

## 🚀 Quick Installation

```bash
pip install py_wise
```

## 🎯 Key Commands

### 1. Smart Dependency Detection
```bash
# Show only packages YOU installed (not auto-dependencies)
py_wise detect

# Generate clean requirements.txt
py_wise detect --output requirements.txt
```

### 2. Venv to Conda Conversion (SINGLE COMMAND!)
```bash
# Convert your current venv to conda environment
py_wise venv-to-conda --name my-project

# With specific Python version
py_wise venv-to-conda --name my-project --python-version 3.11
```

### 3. Hybrid Conda-Pip Resolution
```bash
# Intelligent resolution using both conda and pip
py_wise resolve numpy pandas tensorflow flask

# Force specific strategy
py_wise resolve numpy pandas --strategy conda-only
```

### 4. Docker Optimization
```bash
# Generate optimized Docker configuration
py_wise dockerize

# Generate and build in one command
py_wise dockerize --build --tag my-app:latest
```

### 5. Format Migration
```bash
# Convert between any formats
py_wise migrate requirements.txt --to conda
py_wise migrate environment.yml --to poetry
```

### 6. Multi-Environment Setup
```bash
# Setup dev/staging/prod configurations
py_wise multi-env

# Custom environments
py_wise multi-env -e dev -e test -e staging -e prod
```

## 🔧 Configuration

Create `.py_wise.yml`:

```yaml
detect:
  exclude_packages: [wheel, setuptools, pip]

resolve:
  strategy: hybrid
  prefer_conda: [numpy, scipy, pandas]
  prefer_pip: [flask, django, fastapi]

docker:
  base_image: python:3.11-slim
  optimize: true
```

## 💡 Common Workflows

### Clean Up Messy Project
```bash
py_wise detect --output clean-requirements.txt
py_wise dockerize --optimize
```

### ML Project Setup
```bash
py_wise venv-to-conda --name ml-project
py_wise resolve tensorflow pytorch scikit-learn
```

### Web App Deployment
```bash
py_wise detect --output requirements.txt
py_wise dockerize --build --tag webapp:latest
py_wise multi-env
```

Happy dependency managing! 🎉
