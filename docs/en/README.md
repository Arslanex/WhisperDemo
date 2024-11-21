# Whisper Transcription Module - Installation Guide

## 🚀 Installation Methods

### 1. Regular Installation
For most users who want to use the module:

```bash
# Install from PyPI
pip install whisper-transcriber

# Or install from local directory
pip install .
```

#### When to Use Regular Installation:
- You want to use the module in your projects
- You're an end-user
- You don't plan to modify the package source code

### 2. Editable (Development) Installation
For developers and contributors:

```bash
# Install in editable mode
pip install -e .
```

#### When to Use Editable Installation:
- You are developing the package
- You want to make frequent code changes
- You need to test modifications without reinstalling
- You're contributing to the package development

### 3. Development Dependencies
If you're contributing or running tests:

```bash
# Install with development dependencies
pip install -e .[dev]
```

## 📋 Requirements
- Python 3.8+
- Dependencies:
  - openai-whisper
  - torch
  - numpy
  - soundfile
  - ffmpeg-python

## 🔍 Troubleshooting
- Ensure you have the latest pip version
- Check your Python version compatibility
- Install system dependencies (ffmpeg)

## 🤝 Contributing
- Fork the repository
- Create a virtual environment
- Use editable installation
- Run tests before submitting PRs
