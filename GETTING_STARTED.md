# Getting Started with pywise_pkg Advanced

## 🚀 Quick Installation

```bash
pip install pywise_pkg
```

## 🎯 Key Commands

### 1. Smart Dependency Detection
```bash
# Show only packages YOU installed (not auto-dependencies)
pywise_pkg detect

# Generate clean requirements.txt
pywise_pkg detect --output requirements.txt
```

### 2. Venv to Conda Conversion (SINGLE COMMAND!)
```bash
# Convert your current venv to conda environment
pywise_pkg venv-to-conda --name my-project

# With specific Python version
pywise_pkg venv-to-conda --name my-project --python-version 3.11
```

### 3. Hybrid Conda-Pip Resolution
```bash
# Intelligent resolution using both conda and pip
pywise_pkg resolve numpy pandas tensorflow flask

# Force specific strategy
pywise_pkg resolve numpy pandas --strategy conda-only
```

### 4. Docker Optimization
```bash
# Generate optimized Docker configuration
pywise_pkg dockerize

# Generate and build in one command
pywise_pkg dockerize --build --tag my-app:latest
```

### 5. Format Migration
```bash
# Convert between any formats
pywise_pkg migrate requirements.txt --to conda
pywise_pkg migrate environment.yml --to poetry
```

### 6. Multi-Environment Setup
```bash
# Setup dev/staging/prod configurations
pywise_pkg multi-env

# Custom environments
pywise_pkg multi-env -e dev -e test -e staging -e prod
```

## 🔧 Configuration

Create `.pywise_pkg.yml`:

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
pywise_pkg detect --output clean-requirements.txt
pywise_pkg dockerize --optimize
```

### ML Project Setup
```bash
pywise_pkg venv-to-conda --name ml-project
pywise_pkg resolve tensorflow pytorch scikit-learn
```

### Web App Deployment
```bash
pywise_pkg detect --output requirements.txt
pywise_pkg dockerize --build --tag webapp:latest
pywise_pkg multi-env
```

Happy dependency managing! 🎉
