#!/usr/bin/env python3
"""
Scenario 3: Batch Audio Processing
- Demonstrates processing multiple audio files in a directory
- Supports different output formats
- Handles various model sizes and configurations
"""

from whisper_transcriber import WhisperTranscriber, TranscriptionConfig
import os
import glob

def batch_transcription(input_directory, output_directory='transcriptions', 
                        model_name='small', output_formats=None):
    """
    Perform batch transcription of audio files in a directory
    
    Args:
        input_directory (str): Directory containing audio files
        output_directory (str): Directory to save transcription results
        model_name (str): Whisper model to use
        output_formats (list): List of output formats (txt, srt, json, vtt)
    """
    # Default output formats if not specified
    if output_formats is None:
        output_formats = ['txt', 'srt']
    
    # Create batch processing configuration
    config = TranscriptionConfig(
        model_name=model_name,  # Configurable model size
        task='transcribe',       # Standard transcription
        output_format=output_formats,
        output_dir=output_directory,
        verbose=False            # Minimal logging
    )
    
    # Initialize transcriber
    transcriber = WhisperTranscriber(config)
    
    # Create output directory
    os.makedirs(output_directory, exist_ok=True)
    
    # Find audio files (support multiple extensions)
    audio_extensions = ['*.mp3', '*.wav', '*.m4a', '*.flac', '*.ogg']
    audio_files = []
    for ext in audio_extensions:
        audio_files.extend(glob.glob(os.path.join(input_directory, ext)))
    
    # Process each audio file
    results = {}
    for audio_file in audio_files:
        try:
            print(f"Processing: {audio_file}")
            result = transcriber.transcribe(audio_file)
            results[audio_file] = result
            
            # Optional: Print basic info
            print(f"  Transcribed: {len(result['text'])} characters")
        except Exception as e:
            print(f"Error processing {audio_file}: {e}")
    
    return results

def main():
    # Example usage scenarios
    scenarios = [
        {
            'input_dir': 'podcasts',  # Example directory
            'output_dir': 'podcast_transcripts',
            'model': 'medium',
            'formats': ['txt', 'srt', 'json']
        },
        {
            'input_dir': 'interviews',  # Another example directory
            'output_dir': 'interview_transcripts',
            'model': 'small',
            'formats': ['txt', 'vtt']
        }
    ]
    
    for scenario in scenarios:
        print(f"\n--- Batch Processing: {scenario['input_dir']} ---")
        batch_transcription(
            input_directory=scenario['input_dir'],
            output_directory=scenario['output_dir'],
            model_name=scenario['model'],
            output_formats=scenario['formats']
        )

if __name__ == '__main__':
    main()
