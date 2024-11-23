# Whisper Transcriber - Installation Guide

## Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Operating System: macOS, Linux, or Windows
- Recommended: Virtual environment

## Installation Methods

### 1. Install as Package (Recommended)

#### Using pip
```bash
# Install the latest stable version
pip install whisper-transcriber

# Install with specific version
pip install whisper-transcriber==X.X.X
```

#### Virtual Environment (Recommended)
```bash
# Create a virtual environment
python3 -m venv whisper-env

# Activate virtual environment
# On macOS/Linux
source whisper-env/bin/activate
# On Windows
whisper-env\Scripts\activate

# Install package in virtual environment
pip install whisper-transcriber
```

### 2. Install from Git Repository

#### Clone Repository
```bash
# Clone the repository
git clone https://github.com/your-org/whisper-transcriber.git

# Navigate to project directory
cd whisper-transcriber

# Install in editable mode
pip install -e .
```

### 3. Install Dependencies

#### Core Dependencies
```bash
# Install core dependencies manually
pip install torch
pip install openai-whisper
pip install soundfile
pip install numpy
pip install typing-extensions
```

#### Optional Dependencies
```bash
# GPU Support (CUDA)
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

# Additional audio processing libraries
pip install librosa
```

### 4. FFmpeg Installation

#### macOS (Homebrew)
```bash
# Install Homebrew (if not already installed)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install FFmpeg
brew install ffmpeg
```

#### Linux (Ubuntu/Debian)
```bash
# Update package list
sudo apt update

# Install FFmpeg
sudo apt install ffmpeg
```

#### Linux (Fedora)
```bash
# Install FFmpeg
sudo dnf install ffmpeg
```

#### Windows
1. Download FFmpeg from official website: https://ffmpeg.org/download.html
2. Extract the ZIP file
3. Add the `bin` directory to your system PATH

### 5. Verify Installation

```bash
# Verify Whisper Transcriber installation
pip show whisper-transcriber

# Test basic functionality
whisper-transcribe --help
```

## Troubleshooting

### Common Installation Issues
- Ensure Python version is compatible
- Check pip is up to date: `pip install --upgrade pip`
- Verify all dependencies are installed correctly
- For GPU support, ensure CUDA toolkit is installed

### Performance Considerations
- Larger Whisper models require more computational resources
- GPU acceleration recommended for large audio files
- Choose model size based on your hardware capabilities

## Recommended System Requirements

### Minimum
- CPU: Intel Core i5 or equivalent
- RAM: 8 GB
- Disk Space: 1 GB (for small Whisper models)

### Recommended
- CPU: Intel Core i7 or AMD Ryzen 7
- RAM: 16 GB
- GPU: NVIDIA with CUDA support
- Disk Space: 5 GB (for large Whisper models)

## Notes
- Always use a virtual environment
- Keep dependencies updated
- Check project documentation for the latest installation instructions
