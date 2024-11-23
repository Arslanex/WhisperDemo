# Whisper Transcription Module - Python Module Usage

## Overview
The Whisper Transcription Module provides flexible and programmatic speech-to-text capabilities, directly importable in Python scripts.

## Installation
```bash
pip install whisper-transcriber
```

## Basic Usage

### Simple Transcription
```python
from whisper_transcriber.transcriber import WhisperTranscriber
from whisper_transcriber.config import TranscriptionConfig

# Create configuration
transcription_config = TranscriptionConfig(
    model_name='base',           # Whisper model to use
    verbose=False                # Disable detailed output
)

# Initialize transcriber
whisper_transcriber = WhisperTranscriber(transcription_config)

# Transcribe audio file
transcription_result = whisper_transcriber.transcribe('path/to/audio.mp3')

# Get transcription results
print(transcription_result['text'])  # Full transcription text
print(transcription_result['segments'])  # Detailed segment information
```

## Advanced Configuration

### Detailed Transcription Options
```python
advanced_config = TranscriptionConfig(
    # Model Selection
    model_name='medium',         # Options: tiny, base, small, medium, large
    task='transcribe',           # 'transcribe' or 'translate'
    language='en',               # Language code (optional)
    
    # Quality Control
    temperature=(0.0, 0.2),      # Multiple sampling temperatures
    compression_ratio_threshold=2.4,
    logprob_threshold=-1.0,
    no_speech_threshold=0.6,
    
    # Segment Filtering
    max_segment_length=50,       # Maximum characters per segment
    min_segment_length=10,       # Minimum characters per segment
    
    # Output Configuration
    output_format='srt',         # Output format: txt, json, srt, vtt
    output_dir='./transcriptions' # Output directory
)

# Advanced transcription
advanced_transcriber = WhisperTranscriber(advanced_config)
advanced_result = advanced_transcriber.transcribe('path/to/long_audio.mp3')
```

## Batch Processing

### Transcribe All Audio Files in a Directory
```python
# Transcribe all audio files
batch_config = TranscriptionConfig(
    model_name='small',
    task='transcribe'
)

batch_transcriber = WhisperTranscriber(batch_config)
batch_results = batch_transcriber.process_directory('/path/to/audio/directory')

# Process results
for audio_path, output_path in batch_results.items():
    print(f"Audio: {audio_path}, Transcription: {output_path}")
```

## Error Handling and Logging

### Error Handling Example
```python
try:
    transcription_result = whisper_transcriber.transcribe('problematic_audio.mp3')
except FileNotFoundError:
    print("Audio file not found")
except ValueError as e:
    print(f"Transcription error: {e}")
```

## Performance Tips
- Smaller models are faster but less accurate
- Larger models are slower but more precise
- GPU usage accelerates processing
- Audio quality affects transcription accuracy

## Supported Features
- Multiple model support
- Language translation
- Detailed segment filtering
- Various output formats
- GPU and CPU support

## Translation Mode

### Translate to English
```python
translation_config = TranscriptionConfig(
    task='translate',            # Translate to English
    model_name='medium',         # Recommended model for translation
    language=None                # Auto-detect source language
)

translation_transcriber = WhisperTranscriber(translation_config)
translation_result = translation_transcriber.transcribe('foreign_audio.mp3')
```

## Language Detection

### Automatic Language Detection
```python
auto_detect_config = TranscriptionConfig(
    language=None,               # Enable auto-language detection
    model_name='large'           # Larger models are better at language detection
)
```

## Logging and Debugging

### Enable Verbose Logging
```python
debug_config = TranscriptionConfig(
    verbose=True,                # Enable detailed logging
    model_name='base'            # Choose appropriate model
)
```

## Notes and Best Practices
- Ensure `ffmpeg` is installed for audio processing
- Choose model size based on available computational resources
- Validate audio file quality before transcription
- Use GPU for faster processing when available

## Limitations
- Transcription accuracy depends on:
  - Model size
  - Audio quality
  - Background noise
  - Speaker clarity
- Large audio files may require more processing time
- Some accents or dialects might reduce accuracy
