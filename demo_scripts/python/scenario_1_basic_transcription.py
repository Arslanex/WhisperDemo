#!/usr/bin/env python3
"""
Scenario 1: Basic Audio Transcription
- Demonstrates simple transcription of an audio file
- Uses default 'base' model
- Outputs full transcription text
"""

from whisper_transcriber import WhisperTranscriber, TranscriptionConfig

def basic_transcription(audio_path):
    """
    Perform basic transcription with minimal configuration
    
    Args:
        audio_path (str): Path to the audio file
    """
    # Create basic configuration
    config = TranscriptionConfig(
        model_name='base',      # Smallest, fastest model
        verbose=False           # Disable detailed logging
    )
    
    # Initialize transcriber
    transcriber = WhisperTranscriber(config)
    
    # Transcribe audio
    result = transcriber.transcribe(audio_path)
    
    # Print full transcription
    print("--- Basic Transcription Result ---")
    print(result['text'])
    
    # Optional: Save transcription to file
    with open('basic_transcription.txt', 'w') as f:
        f.write(result['text'])

def main():
    # Path to demo audio file
    audio_file = '../demo.mp3'
    basic_transcription(audio_file)

if __name__ == '__main__':
    main()
