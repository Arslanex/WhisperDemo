#!/usr/bin/env python3
"""
Scenario 4: Advanced Transcription Configuration
- Demonstrates fine-grained control over transcription process
- Implements quality control and segment filtering
- Shows how to handle challenging audio scenarios
"""

from whisper_transcriber import WhisperTranscriber, TranscriptionConfig
import logging

def advanced_transcription(audio_path, 
                           model_name='medium', 
                           language=None, 
                           temperature_range=None):
    """
    Perform advanced transcription with detailed configuration
    
    Args:
        audio_path (str): Path to the audio file
        model_name (str): Whisper model to use
        language (str, optional): Specific language code
        temperature_range (tuple, optional): Sampling temperature range
    """
    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s: %(message)s',
        filename='transcription_log.txt'
    )
    
    # Default temperature range if not provided
    if temperature_range is None:
        temperature_range = (0.0, 0.2, 0.4)
    
    # Create advanced configuration
    config = TranscriptionConfig(
        # Model Selection
        model_name=model_name,
        task='transcribe',
        language=language,
        
        # Quality Control Parameters
        temperature=temperature_range,  # Multiple sampling temperatures
        compression_ratio_threshold=2.4,
        logprob_threshold=-1.0,
        no_speech_threshold=0.6,
        
        # Segment Filtering
        max_segment_length=50,   # Maximum characters per segment
        min_segment_length=10,   # Minimum characters per segment
        
        # Output Configuration
        output_format=['txt', 'srt', 'json'],
        word_timestamps=True,
        verbose=True
    )
    
    # Initialize transcriber
    transcriber = WhisperTranscriber(config)
    
    try:
        # Transcribe audio with advanced settings
        result = transcriber.transcribe(audio_path)
        
        # Detailed logging and analysis
        logging.info(f"Transcription completed for {audio_path}")
        logging.info(f"Total segments: {len(result.get('segments', []))}")
        
        # Print segment-level details
        print("\n--- Segment Analysis ---")
        for segment in result.get('segments', []):
            print(f"Segment {segment['id']}:")
            print(f"  Text: {segment['text']}")
            print(f"  Start: {segment['start']:.2f}s")
            print(f"  End: {segment['end']:.2f}s")
            print(f"  Confidence: {segment.get('avg_logprob', 'N/A')}")
        
        return result
    
    except Exception as e:
        logging.error(f"Transcription failed: {e}")
        print(f"Error during transcription: {e}")
        return None

def main():
    # Scenarios demonstrating different configurations
    scenarios = [
        {
            'audio_path': 'demo.mp3',
            'model_name': 'medium',
            'language': None,  # Auto-detect
            'temperature_range': (0.0, 0.2)
        },
        {
            'audio_path': 'noisy_recording.mp3',
            'model_name': 'large',
            'language': 'en',
            'temperature_range': (0.0, 0.2, 0.4)
        }
    ]
    
    for scenario in scenarios:
        print(f"\n--- Processing: {scenario['audio_path']} ---")
        advanced_transcription(**scenario)

if __name__ == '__main__':
    main()
