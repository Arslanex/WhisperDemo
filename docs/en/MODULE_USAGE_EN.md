# Whisper Transcription Module - Python Module Usage

## Overview
The Whisper Transcription Module can be imported and used directly in Python scripts, offering flexible and programmatic audio transcription.

## Installation
```bash
pip install whisper-transcriber
```

## Basic Usage

### Simple Transcription
```python
from whisper_transcriber import WhisperTranscriber, TranscriptionConfig

# Create a configuration
config = TranscriptionConfig(
    model='base',           # Whisper model to use
    language='en',          # Optional: specify language
    verbose=False           # Disable verbose output
)

# Initialize transcriber
transcriber = WhisperTranscriber(config)

# Transcribe an audio file
result = transcriber.transcribe('path/to/audio.mp3')

# Access transcription results
print(result.text)  # Full transcription text
print(result.segments)  # Detailed segment information
```

## Advanced Configuration

### Detailed Transcription Options
```python
config = TranscriptionConfig(
    # Model Selection
    model='medium',         # Choose from: tiny, base, small, medium, large
    task='transcribe',      # 'transcribe' or 'translate'
    
    # Quality Control
    temperature=[0.0, 0.2],  # Multiple sampling temperatures
    compression_ratio_threshold=2.4,
    log_prob_threshold=-1.0,
    no_speech_threshold=0.6,
    
    # Segment Filtering
    max_segment_length=50,  # Maximum characters per segment
    min_segment_length=10,  # Minimum characters per segment
    
    # Output Formatting
    word_timestamps=True,   # Enable word-level timing
    verbose=True            # Detailed logging
)
```

### Output Handling
```python
# Generate multiple output formats
transcriber.generate_outputs(
    result, 
    output_dir='./transcriptions',
    formats=['srt', 'txt', 'json']
)
```

## Advanced Features

### Language Detection
```python
# Automatic language detection
config = TranscriptionConfig(language=None)  # Auto-detect
```

### Translation Mode
```python
config = TranscriptionConfig(
    task='translate',       # Translate to English
    model='medium'          # Recommended for translation
)
```

## Error Handling
```python
try:
    result = transcriber.transcribe('audio.mp3')
except Exception as e:
    print(f"Transcription error: {e}")
```

## Performance Considerations
- Larger models provide better accuracy but require more computational resources
- CPU vs GPU performance varies
- Recommended to use smaller models for quick transcriptions
- Large models best for high-accuracy requirements

## Logging and Debugging
```python
config = TranscriptionConfig(verbose=True)
# Enables detailed logging of transcription process
```

## Notes
- Ensure `ffmpeg` is installed for audio processing
- Some features may require additional dependencies
- Performance depends on audio quality, model size, and system resources
