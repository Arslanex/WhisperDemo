# Whisper Transcription Module

A simple and scalable Python module for audio transcription using OpenAI's Whisper model.

## 🌟 Overview

Whisper Transcription Module is a powerful, flexible tool for converting audio to text using state-of-the-art machine learning technology. Leveraging OpenAI's Whisper model, it provides robust transcription capabilities across multiple languages and audio formats.

## 📦 Features

- 🔊 Audio transcription using OpenAI's Whisper model
- 🌐 Multi-language support
- 📄 Multiple output formats (TXT, JSON, SRT, VTT)
- 📂 Batch processing of audio files
- 🖥️ Intuitive command-line interface
- ⚙️ Highly configurable transcription settings

## 📚 Documentation

### 🇺🇸 English Documentation
- [CLI Usage Guide](docs/en/README.md)
- [Module Usage Guide](docs/en/MODULE_USAGE_EN.md)
- [Feature Specifications](docs/en/FEATURES_EN.md)

### 🇹🇷 Türkçe Dokümantasyon
- [Komut Satırı Kullanım Kılavuzu](docs/tr/README.md)
- [Modül Kullanım Kılavuzu](docs/tr/MODULE_USAGE_TR.md)
- [Özellik Spesifikasyonları](docs/tr/FEATURES_TR.md)

## 🚀 Quick Start

### Installation
```bash
# Install from PyPI
pip install whisper-transcriber

# Or install from local directory
pip install .
```

### Basic Usage
```bash
# Transcribe an audio file
python -m whisper_transcriber audio.mp3
```

## 📋 Requirements
- Python 3.8+
- Dependencies:
  - openai-whisper
  - torch
  - numpy
  - soundfile
  - ffmpeg-python

### 💻 Computational Resources
- **CPU Support**: All models
- **GPU Acceleration**: Optional, improves performance
  - Use `--device cuda` for GPU transcription
  - Automatic fallback to CPU if CUDA unavailable

## 🤝 Contributing
1. Fork the repository
2. Create a virtual environment
3. Install development dependencies: `pip install -e .[dev]`
4. Run tests: `pytest`
5. Submit a pull request

## 🐛 Support
- [Open an Issue](https://github.com/yourusername/WhisperDemo/issues)
- Check our [Troubleshooting Guide](docs/en/TROUBLESHOOTING.md)

## 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgements
- OpenAI for the Whisper model
- Python open-source community
