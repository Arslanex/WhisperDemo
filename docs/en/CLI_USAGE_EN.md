# Whisper Transcriber - Command Line Interface (CLI) Usage Guide

## Overview
The Whisper Transcriber CLI provides a powerful, user-friendly interface for transcribing audio files directly from the command line.

## Installation
```bash
pip install whisper-transcriber
```

## Basic Usage

### Simple Transcription
```bash
# Basic transcription of an audio file
whisper-transcribe audio_file.mp3

# Specify output directory
whisper-transcribe audio_file.mp3 --output-dir ./transcriptions
```

## Advanced Usage

### Model and Language Selection
```bash
# Choose specific Whisper model
whisper-transcribe audio_file.mp3 --model medium

# Specify source language
whisper-transcribe audio_file.mp3 --language en

# Translate to English
whisper-transcribe audio_file.mp3 --task translate
```

## Output Formats

### Multiple Output Formats
```bash
# Generate multiple output formats
whisper-transcribe audio_file.mp3 --output-format srt txt json

# Specify custom output directory
whisper-transcribe audio_file.mp3 --output-dir ./transcriptions --output-format vtt
```

## Batch Processing

### Transcribe Multiple Files
```bash
# Transcribe all audio files in a directory
whisper-transcribe /path/to/audio/directory/* --recursive

# Batch process with specific model
whisper-transcribe /path/to/audio/directory/* --model small --recursive
```

## Performance and Quality Control

### Advanced Configuration
```bash
# Control transcription quality
whisper-transcribe audio_file.mp3 \
    --temperature 0.0 0.2 \
    --compression-ratio-threshold 2.4 \
    --logprob-threshold -1.0 \
    --no-speech-threshold 0.6

# Segment length control
whisper-transcribe audio_file.mp3 \
    --max-segment-length 50 \
    --min-segment-length 10
```

## Logging and Debugging

### Verbose Output
```bash
# Enable detailed logging
whisper-transcribe audio_file.mp3 --verbose

# Save log to file
whisper-transcribe audio_file.mp3 --verbose --log-file transcription.log
```

## GPU and Performance

### GPU Acceleration
```bash
# Use GPU for faster processing
whisper-transcribe audio_file.mp3 --device cuda

# Specify GPU device
whisper-transcribe audio_file.mp3 --device cuda:0
```

## Common Options

### Full Command Reference
```bash
whisper-transcribe [OPTIONS] INPUT_FILE

Options:
  --model TEXT            Whisper model to use (tiny/base/small/medium/large)
  --task TEXT             Transcription task (transcribe/translate)
  --language TEXT         Source language code
  --output-dir TEXT       Output directory for transcription files
  --output-format TEXT    Output file formats (txt/srt/json/vtt)
  --device TEXT           Processing device (cpu/cuda)
  --verbose              Enable detailed logging
  --log-file TEXT         Path to log file
  --temperature FLOAT    Sampling temperature
  --max-segment-length INT Maximum segment length
  --min-segment-length INT Minimum segment length
  --recursive            Process all files in directory
  --help                 Show this help message
```

## Examples

### Real-World Scenarios
```bash
# Transcribe podcast episode
whisper-transcribe podcast.mp3 --model medium --language en --output-format srt txt

# Translate foreign language video
whisper-transcribe foreign_video.mp4 --task translate --model large

# Batch process interview recordings
whisper-transcribe /path/to/interviews/* --recursive --model small
```

## Troubleshooting

### Common Issues
- Ensure `ffmpeg` is installed
- Check audio file format and quality
- Verify sufficient disk space
- Use appropriate model for your hardware

## Performance Tips
- Smaller models are faster but less accurate
- Use GPU for large files or complex transcriptions
- Validate audio quality before transcription

## Limitations
- Transcription accuracy varies with:
  - Model size
  - Audio quality
  - Background noise
  - Speaker clarity
- Large files may require more processing time
- Some accents might reduce accuracy

## Notes
- Supports most audio and video formats
- Requires Python 3.8+
- GPU acceleration recommended for large files
