#!/usr/bin/env python3
"""
Scenario 5: Robust Error Handling and Fallback Strategies
- Demonstrates handling various transcription challenges
- Implements multiple fallback mechanisms
- Shows how to gracefully handle different audio input scenarios
"""

from whisper_transcriber import WhisperTranscriber, TranscriptionConfig
import os
import logging
from typing import Optional, Dict, Any

class TranscriptionHandler:
    def __init__(self, log_file='transcription_errors.log'):
        """
        Initialize transcription handler with logging
        
        Args:
            log_file (str): Path to log file for error tracking
        """
        # Configure logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s: %(message)s',
            filename=log_file,
            filemode='a'
        )
        self.logger = logging.getLogger()
    
    def transcribe_with_fallback(self, 
                                 audio_path: str, 
                                 fallback_models: list = None) -> Optional[Dict[str, Any]]:
        """
        Transcribe audio with multiple fallback strategies
        
        Args:
            audio_path (str): Path to the audio file
            fallback_models (list): List of models to try if initial transcription fails
        
        Returns:
            Transcription result or None if all attempts fail
        """
        # Default fallback models from smallest to largest
        if fallback_models is None:
            fallback_models = ['base', 'small', 'medium', 'large']
        
        # Validate audio file
        if not os.path.exists(audio_path):
            self.logger.error(f"Audio file not found: {audio_path}")
            return None
        
        # Check file size and type
        file_size = os.path.getsize(audio_path)
        file_extension = os.path.splitext(audio_path)[1].lower()
        
        if file_size == 0:
            self.logger.error(f"Empty audio file: {audio_path}")
            return None
        
        supported_extensions = ['.mp3', '.wav', '.m4a', '.flac', '.ogg']
        if file_extension not in supported_extensions:
            self.logger.warning(f"Unsupported file type: {file_extension}")
        
        # Attempt transcription with fallback models
        for model_name in fallback_models:
            try:
                self.logger.info(f"Attempting transcription with {model_name} model")
                
                # Create configuration with current model
                config = TranscriptionConfig(
                    model_name=model_name,
                    task='transcribe',
                    verbose=False,
                    
                    # Quality control parameters
                    compression_ratio_threshold=2.4,
                    logprob_threshold=-1.0,
                    no_speech_threshold=0.6
                )
                
                # Initialize transcriber
                transcriber = WhisperTranscriber(config)
                
                # Attempt transcription
                result = transcriber.transcribe(audio_path)
                
                # Basic result validation
                if result and result.get('text'):
                    self.logger.info(f"Successfully transcribed with {model_name} model")
                    return result
                
            except Exception as e:
                self.logger.warning(f"Transcription failed with {model_name} model: {e}")
        
        # If all models fail
        self.logger.error(f"Transcription failed for all models: {audio_path}")
        return None
    
    def process_audio_directory(self, 
                                input_directory: str, 
                                output_directory: str = 'transcriptions'):
        """
        Process all audio files in a directory with error handling
        
        Args:
            input_directory (str): Directory containing audio files
            output_directory (str): Directory to save transcription results
        """
        # Create output directory if not exists
        os.makedirs(output_directory, exist_ok=True)
        
        # Supported audio extensions
        audio_extensions = ['.mp3', '.wav', '.m4a', '.flac', '.ogg']
        
        # Process each file in the directory
        for filename in os.listdir(input_directory):
            file_path = os.path.join(input_directory, filename)
            
            # Check if it's a file with supported audio extension
            if os.path.isfile(file_path) and os.path.splitext(filename)[1].lower() in audio_extensions:
                print(f"Processing: {filename}")
                
                # Transcribe with fallback
                result = self.transcribe_with_fallback(file_path)
                
                if result:
                    # Save transcription
                    output_file = os.path.join(output_directory, f"{os.path.splitext(filename)[0]}_transcript.txt")
                    with open(output_file, 'w') as f:
                        f.write(result['text'])
                    print(f"  Saved transcript: {output_file}")
                else:
                    print(f"  Failed to transcribe: {filename}")

def main():
    # Create transcription handler
    handler = TranscriptionHandler()
    
    # Example scenarios
    scenarios = [
        {
            'input_dir': 'problematic_audio',
            'output_dir': 'robust_transcriptions'
        }
    ]
    
    # Process each scenario
    for scenario in scenarios:
        print(f"\n--- Processing Directory: {scenario['input_dir']} ---")
        handler.process_audio_directory(
            input_directory=scenario['input_dir'],
            output_directory=scenario['output_dir']
        )

if __name__ == '__main__':
    main()
