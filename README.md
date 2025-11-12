# py_wise - Intelligent Python Dependency Management

🚀 **The smartest way to manage Python dependencies with conda-pip hybrid support!**

py_wise goes beyond traditional dependency management by intelligently distinguishing between packages YOU installed and auto-installed dependencies, while providing seamless conda-pip integration and advanced environment management.

## 🌟 Key Features

### 🧠 Smart Dependency Detection
- **Primary Package Detection**: Unlike `pip freeze`, shows only packages YOU installed
- **Dependency Intelligence**: Understands which packages are auto-dependencies
- **Cross-Platform**: Works with pip, conda, poetry, and pipenv environments

### 🔄 Conda-Pip Hybrid Support
- **Intelligent Resolution**: Automatically chooses optimal package source (conda vs pip)
- **Hybrid Environments**: Creates conda environments with pip packages when needed
- **Single Command Conversion**: `py_wise venv-to-conda` - converts venv to conda instantly!

### 🐳 Docker Integration
- **Optimized Dockerfiles**: Generates production-ready Docker configurations
- **Multi-stage Builds**: Reduces image size automatically
- **Framework Detection**: Auto-configures for Django, Flask, FastAPI, etc.

### 🔧 Environment Migration
- **Format Conversion**: Convert between requirements.txt ↔ environment.yml ↔ pyproject.toml
- **Multi-Environment Setup**: Create dev/staging/prod configs with one command
- **Configuration Management**: Manage multiple environment configurations

## 🚀 Quick Start

### Installation

```bash
pip install py_wise
```

### Core Commands

```bash
# 🔍 Show only PRIMARY packages (not dependencies!)
py_wise detect

# 🔄 Convert your venv to conda environment (SINGLE COMMAND!)
py_wise venv-to-conda --name my-project

# 🧠 Resolve dependencies with conda-pip hybrid intelligence
py_wise resolve numpy pandas tensorflow

# 🐳 Generate optimized Docker configuration
py_wise dockerize --build --tag my-app:latest

# 📦 Migrate between any dependency formats
py_wise migrate requirements.txt --to conda

# 🏗️ Setup multi-environment configuration
py_wise multi-env --environments dev staging prod
```

## 💡 Why py_wise?

### Before py_wise:
```bash
$ pip freeze > requirements.txt
# 😱 Creates 50+ line file with every dependency!
numpy==1.21.0
pandas==1.3.0
python-dateutil==2.8.2  # ← Auto-dependency
pytz==2021.1            # ← Auto-dependency
six==1.16.0             # ← Auto-dependency
# ... 45 more lines of dependencies you never installed!
```

### With py_wise:
```bash
$ py_wise detect --output requirements.txt
# ✨ Creates clean file with only YOUR packages!
numpy==1.21.0
pandas==1.3.0
# Done! Only packages YOU actually installed
```

## 🔥 Advanced Features

### Single-Command Environment Conversion

```bash
# Convert your current venv to conda with hybrid optimization
py_wise venv-to-conda --name my-project
# ✅ Analyzes packages for optimal conda vs pip installation
# ✅ Creates environment.yml with hybrid dependencies
# ✅ Sets up new conda environment
# ✅ Provides activation commands
```

### Intelligent Hybrid Resolution

```bash
# Let py_wise decide the best package source
py_wise resolve numpy scipy tensorflow flask
# 📊 numpy, scipy → conda (better performance)
# 📦 tensorflow → conda (GPU support)  
# 🐍 flask → pip (better ecosystem fit)
```

### Docker Optimization

```bash
# Generate production-ready Docker setup
py_wise dockerize --optimize --build --tag my-app:latest
# 🐳 Analyzes your packages for optimal base image
# 🔧 Adds required system dependencies
# 📦 Creates multi-stage build for size optimization
# 🚀 Builds and tags the image
```

### Multi-Environment Management

```bash
# Setup dev/staging/prod configurations
py_wise multi-env
# 📁 Creates requirements-dev.txt, requirements-staging.txt, requirements-prod.txt
# ⚙️ Configures environment-specific variables
# 🐳 Generates Docker configs for each environment
```

## 📋 Command Reference

| Command | Description | Example |
|---------|-------------|---------|
| `detect` | Show primary packages only | `py_wise detect --output clean-requirements.txt` |
| `venv-to-conda` | Convert venv to conda | `py_wise venv-to-conda --name myproject` |
| `resolve` | Hybrid dependency resolution | `py_wise resolve numpy pandas --strategy hybrid` |
| `migrate` | Convert between formats | `py_wise migrate requirements.txt --to conda` |
| `dockerize` | Generate Docker config | `py_wise dockerize --build --tag app:latest` |
| `multi-env` | Setup multiple environments | `py_wise multi-env -e dev -e prod` |

## 🔧 Configuration

Create `.py_wise.yml` in your project root:

```yaml
# Dependency detection
detect:
  exclude_packages: [wheel, setuptools, pip]
  include_dev: false

# Hybrid resolution preferences  
resolve:
  strategy: hybrid  # conda for ML/scientific, pip for web
  prefer_conda: [numpy, scipy, pandas, tensorflow]
  prefer_pip: [flask, django, fastapi, requests]

# Docker optimization
docker:
  base_image: python:3.11-slim
  multi_stage: true
  optimize_layers: true
```

## 🎯 Use Cases

### 🧪 Data Scientists
```bash
# Perfect for ML environments with complex dependencies
py_wise venv-to-conda --name ml-project
py_wise resolve tensorflow pytorch scikit-learn
```

### 🌐 Web Developers
```bash
# Clean up messy Django/Flask projects
py_wise detect --output clean-requirements.txt
py_wise dockerize --framework django
```

### 🚀 DevOps Engineers
```bash
# Standardize environments across team
py_wise multi-env --environments dev test staging prod
py_wise dockerize --optimize --build
```

### 📦 Package Maintainers
```bash
# Generate clean dependencies for PyPI
py_wise detect --format poetry --output pyproject.toml
```

## 🏗️ Development

```bash
git clone https://github.com/py_wise/py_wise.git
cd py_wise
pip install -e .[dev]
pytest
```

## 🤝 Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## 📄 License

MIT License - see [LICENSE](LICENSE) file.

## 🙏 Acknowledgments

- Built on excellent Python packaging ecosystem
- Inspired by conda, pip, poetry, and pipenv
- Thanks to the Python community for feedback

## 🚀 Roadmap

- [ ] GUI interface for dependency management
- [ ] VS Code extension
- [ ] Automatic security vulnerability scanning
- [ ] AI-powered dependency optimization
- [ ] Integration with CI/CD platforms
- [ ] Support for private package repositories

---

**⭐ Star this repo if py_wise helps you manage dependencies better!**

*Made with ❤️ for the Python community*
