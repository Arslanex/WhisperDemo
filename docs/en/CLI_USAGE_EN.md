# Whisper Transcription Module - CLI Usage

## Overview
The Whisper Transcription Module provides a powerful command-line interface for transcribing audio files with advanced configuration options.

## Basic Usage
```bash
python -m whisper_transcriber [OPTIONS] INPUT_FILE
```

## Command-Line Options

### Basic Transcription Options
- `INPUT_FILE`: Path to the audio file to be transcribed (required)
- `-o, --output-dir`: Directory to save transcription files (default: current directory)
- `-m, --model`: Whisper model to use (default: 'base')
  - Choices: 'tiny', 'base', 'small', 'medium', 'large'

### Advanced Transcription Configuration
- `--language`: Specify audio language (optional, auto-detect if not provided)
- `--task`: Transcription task type (default: 'transcribe')
  - Choices: 'transcribe', 'translate'
- `--verbose`: Enable verbose output
- `--temperature`: Sampling temperature for transcription (default: 0.0)
  - Multiple temperatures can be specified: `--temperature 0.0 0.2 0.4`

### Filtering and Quality Control
- `--compression-ratio-threshold`: Maximum compression ratio allowed
- `--log-prob-threshold`: Minimum log probability for segment inclusion
- `--no-speech-threshold`: Threshold for detecting non-speech segments
- `--max-segment-length`: Maximum length of transcription segments
- `--min-segment-length`: Minimum length of transcription segments

### Output Format Options
- `--output-formats`: Specify output file formats
  - Choices: 'txt', 'srt', 'vtt', 'json'
  - Example: `--output-formats srt txt`
- `--word-timestamps`: Enable word-level timestamps

## Examples

### Basic Transcription
```bash
python -m whisper_transcriber audio.mp3
```

### Advanced Transcription with Multiple Options
```bash
python -m whisper_transcriber audio.mp3 \
    --model medium \
    --language en \
    --output-dir ./transcriptions \
    --output-formats srt txt \
    --word-timestamps \
    --temperature 0.0 0.2 \
    --max-segment-length 50
```

## Notes
- Ensure you have the required dependencies installed
- Large models may require significant computational resources
- Performance varies based on audio quality and model size
