"""Whisper Transcription Module

A simple and scalable module for audio transcription using OpenAI's Whisper.
"""

from .config import TranscriptionConfig
from .transcriber import WhisperTranscriber, main
from .output_handler import OutputHandler

__version__ = "0.1.0"
__all__ = ["TranscriptionConfig", "WhisperTranscriber", "OutputHandler", "main"]
