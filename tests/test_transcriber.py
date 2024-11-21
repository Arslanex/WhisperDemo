import pytest
from pathlib import Path
from whisper_transcriber import WhisperTranscriber, TranscriptionConfig

def test_transcriber_initialization():
    """Test that the transcriber initializes correctly."""
    config = TranscriptionConfig(model_name="base")
    transcriber = WhisperTranscriber(config)
    assert transcriber.config.model_name == "base"
    assert transcriber.model is not None

def test_invalid_model():
    """Test that invalid model names raise an error."""
    config = TranscriptionConfig(model_name="invalid_model")
    with pytest.raises(ValueError):
        WhisperTranscriber(config)

def test_invalid_audio_file():
    """Test that invalid audio files raise an error."""
    config = TranscriptionConfig()
    transcriber = WhisperTranscriber(config)
    with pytest.raises(FileNotFoundError):
        transcriber.transcribe("nonexistent.wav")

def test_invalid_directory():
    """Test that invalid directories raise an error."""
    config = TranscriptionConfig()
    transcriber = WhisperTranscriber(config)
    with pytest.raises(NotADirectoryError):
        transcriber.process_directory("nonexistent_dir")
