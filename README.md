# 🎙️ Whisper Transcription Module

## 🌟 Overview

A powerful, flexible Python module for audio transcription leveraging OpenAI's Whisper model, designed to transform audio content into accurate, multilingual text.

## ✨ Key Features

- 🔊 **Advanced Audio Transcription**
  - Utilizes state-of-the-art Whisper AI technology
  - Supports multiple languages and dialects

- 🌐 **Multilingual Support**
  - Transcribe and translate audio across 99 languages
  - Automatic language detection

- 📄 **Flexible Output Formats**
  - TXT, JSON, SRT, VTT
  - Customizable transcription settings

- 📂 **Versatile Processing**
  - Single file and batch processing
  - Configurable model sizes
  - GPU and CPU support

  
## 📚 Documentation
| 🇺🇸 English| 🇹🇷 Türkçe |
|-------------------------------------------------|-------------|
| [Installation Guide](docs/en/README.md)| [Installation Guide](docs/en/README.md)|
| [CLI Usage Guide](docs/en/README.md)|[Komut Satırı Kullanım Kılavuzu](docs/tr/README.md) |
| [Module Usage Guide](docs/en/MODULE_USAGE_EN.md)| [Modül Kullanım Kılavuzu](docs/tr/MODULE_USAGE_TR.md) |
| [Feature Specifications](docs/en/FEATURES_EN.md)| [Özellik Spesifikasyonları](docs/tr/FEATURES_TR.md)|

## 🚀 Demo Scripts

The `demo_scripts` directory offers comprehensive scenarios demonstrating the module's capabilities:

| Scenario | Description | Key Features |
|----------|-------------|--------------|
| 1: Basic Transcription | Simple audio transcription | Default 'base' model, quick processing |
| 2: Multilingual Translation | Translate audio to English | Multi-language support, configurable logging |
| 3: Batch Processing | Process multiple audio files | Directory-wide transcription, format flexibility |
| 4: Advanced Configuration | Detailed transcription control | Quality filtering, segment management |
| 5: Error Handling | Robust error management | Fallback strategies, comprehensive logging |
| 6: Advanced Batch Processing | Large-scale transcription | Parallel processing, detailed reporting |

## 📋 System Requirements

### 💻 Computational Resources
- **Python**: 3.8+
- **CPU**: All models supported
- **GPU**: Optional acceleration
  - Use `--device cuda` for GPU transcription
  - Automatic CPU fallback

### 📦 Dependencies
- openai-whisper
- torch
- numpy
- soundfile
- ffmpeg-python

## 🤝 Contributing

1. Fork the repository
2. Create a virtual environment
3. Install development dependencies: `pip install -e .[dev]`
4. Run tests: `pytest`
5. Submit a pull request

## 🐛 Support

- [Open an Issue](https://github.com/yourusername/WhisperDemo/issues)
- Consult [Troubleshooting Guide](docs/en/TROUBLESHOOTING.md)

## 📄 License

MIT License - see the LICENSE file for details.

## 🙏 Acknowledgements

- OpenAI for the Whisper model
- Python open-source community
