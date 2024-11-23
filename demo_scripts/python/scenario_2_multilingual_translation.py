#!/usr/bin/env python3
"""
Scenario 2: Multilingual Translation and Transcription
- Demonstrates translation of audio from one language to English
- Uses larger model for better accuracy
- Handles multiple language inputs
"""

from whisper_transcriber import WhisperTranscriber, TranscriptionConfig
import os

def multilingual_translation(audio_path, source_language=None):
    """
    Perform translation from source language to English
    
    Args:
        audio_path (str): Path to the audio file
        source_language (str, optional): Source language code. 
                                         None for auto-detection
    """
    # Create translation configuration
    config = TranscriptionConfig(
        model_name='medium',    # Recommended for translation
        task='translate',        # Translate to English
        language=source_language,  # Auto-detect if None
        verbose=True             # Detailed logging
    )
    
    # Initialize transcriber
    transcriber = WhisperTranscriber(config)
    
    # Transcribe and translate audio
    result = transcriber.transcribe(audio_path)
    
    # Print translation details
    print("--- Multilingual Translation ---")
    print(f"Original Language: {result.get('detected_language', 'Auto-detected')}")
    print("Translated Text:")
    print(result['text'])
    
    # Create output directory if not exists
    os.makedirs('translations', exist_ok=True)
    
    # Save translation to file
    output_file = f"translations/translation_{os.path.basename(audio_path)}.txt"
    with open(output_file, 'w') as f:
        f.write(result['text'])
    
    return result

def main():
    # Example audio files (replace with actual paths)
    audio_files = [
        'demo.mp3',  # Default auto-detect
        # Add paths to multilingual audio files here
    ]
    
    for audio_file in audio_files:
        print(f"\nProcessing: {audio_file}")
        multilingual_translation(audio_file)

if __name__ == '__main__':
    main()
