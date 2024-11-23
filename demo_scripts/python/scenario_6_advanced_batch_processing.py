#!/usr/bin/env python3
"""
Scenario 6: Advanced Batch Processing for Audio Transcription
- Supports parallel processing of audio files
- Generates comprehensive transcription reports
- Provides flexible configuration for batch jobs
- Handles large-scale audio transcription scenarios
"""

import os
import csv
import json
import logging
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import List, Dict, Any, Optional

from whisper_transcriber import WhisperTranscriber, TranscriptionConfig

class AdvancedBatchTranscriber:
    def __init__(self, 
                 log_file: str = 'batch_transcription.log', 
                 max_workers: int = None):
        """
        Initialize advanced batch transcription handler
        
        Args:
            log_file (str): Path to log file for batch processing
            max_workers (int): Number of parallel workers for processing
        """
        # Configure logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s: %(message)s',
            filename=log_file,
            filemode='w'
        )
        self.logger = logging.getLogger()
        
        # Set max workers (defaults to number of CPU cores if not specified)
        self.max_workers = max_workers or os.cpu_count()
        
    def _transcribe_single_file(self, 
                                 audio_path: str, 
                                 config: TranscriptionConfig) -> Dict[str, Any]:
        """
        Transcribe a single audio file
        
        Args:
            audio_path (str): Path to the audio file
            config (TranscriptionConfig): Transcription configuration
        
        Returns:
            Dictionary with transcription results and metadata
        """
        try:
            # Validate file
            if not os.path.exists(audio_path):
                raise FileNotFoundError(f"Audio file not found: {audio_path}")
            
            # Initialize transcriber
            transcriber = WhisperTranscriber(config)
            
            # Transcribe
            result = transcriber.transcribe(audio_path)
            
            # Prepare result with additional metadata
            return {
                'file_path': audio_path,
                'success': True,
                'text': result.get('text', ''),
                'language': result.get('language', 'unknown'),
                'duration': result.get('duration', 0),
                'segments': len(result.get('segments', []))
            }
        
        except Exception as e:
            self.logger.error(f"Transcription failed for {audio_path}: {e}")
            return {
                'file_path': audio_path,
                'success': False,
                'error': str(e)
            }
    
    def batch_transcribe(self, 
                         input_directory: str, 
                         output_directory: str = 'batch_transcriptions',
                         model_name: str = 'base',
                         language: Optional[str] = None,
                         task: str = 'transcribe') -> Dict[str, Any]:
        """
        Batch transcribe all supported audio files in a directory
        
        Args:
            input_directory (str): Directory containing audio files
            output_directory (str): Directory to save transcription results
            model_name (str): Whisper model to use
            language (str, optional): Source language of audio
            task (str): Transcription task (transcribe or translate)
        
        Returns:
            Summary of batch processing results
        """
        # Create output directories
        os.makedirs(output_directory, exist_ok=True)
        os.makedirs(os.path.join(output_directory, 'transcripts'), exist_ok=True)
        os.makedirs(os.path.join(output_directory, 'reports'), exist_ok=True)
        
        # Supported audio extensions
        audio_extensions = ['.mp3', '.wav', '.m4a', '.flac', '.ogg']
        
        # Collect audio files
        audio_files = [
            os.path.join(input_directory, f) 
            for f in os.listdir(input_directory) 
            if os.path.isfile(os.path.join(input_directory, f)) 
            and os.path.splitext(f)[1].lower() in audio_extensions
        ]
        
        # Prepare configuration
        config = TranscriptionConfig(
            model_name=model_name,
            task=task,
            language=language,
            verbose=False
        )
        
        # Results storage
        results = []
        
        # Parallel processing
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            # Submit transcription jobs
            future_to_file = {
                executor.submit(self._transcribe_single_file, file_path, config): file_path 
                for file_path in audio_files
            }
            
            # Process results as they complete
            for future in as_completed(future_to_file):
                result = future.result()
                results.append(result)
                
                if result['success']:
                    # Save transcript
                    filename = os.path.basename(result['file_path'])
                    transcript_path = os.path.join(
                        output_directory, 
                        'transcripts', 
                        f"{os.path.splitext(filename)[0]}_transcript.txt"
                    )
                    with open(transcript_path, 'w', encoding='utf-8') as f:
                        f.write(result['text'])
        
        # Generate batch report
        batch_summary = {
            'total_files': len(audio_files),
            'successful_transcriptions': sum(1 for r in results if r['success']),
            'failed_transcriptions': sum(1 for r in results if not r['success']),
            'model_used': model_name,
            'task': task
        }
        
        # Save detailed report
        report_path = os.path.join(output_directory, 'reports', 'batch_report.json')
        with open(report_path, 'w') as f:
            json.dump({
                'summary': batch_summary,
                'detailed_results': results
            }, f, indent=2)
        
        # Save CSV report for easy spreadsheet viewing
        csv_path = os.path.join(output_directory, 'reports', 'batch_report.csv')
        with open(csv_path, 'w', newline='', encoding='utf-8') as f:
            csv_writer = csv.DictWriter(f, fieldnames=[
                'file_path', 'success', 'text', 'language', 
                'duration', 'segments', 'error'
            ])
            csv_writer.writeheader()
            csv_writer.writerows(results)
        
        # Log summary
        self.logger.info(f"Batch Transcription Complete: {batch_summary}")
        
        return batch_summary

def main():
    # Create batch transcriber
    batch_transcriber = AdvancedBatchTranscriber()
    
    # Define batch processing scenarios
    scenarios = [
        {
            'input_dir': 'audio_samples',
            'output_dir': 'multilingual_transcriptions',
            'model_name': 'small',
            'language': None,  # Auto-detect
            'task': 'transcribe'
        },
        {
            'input_dir': 'english_podcasts',
            'output_dir': 'podcast_transcriptions',
            'model_name': 'medium',
            'language': 'en',
            'task': 'transcribe'
        }
    ]
    
    # Process each scenario
    for scenario in scenarios:
        print(f"\n--- Processing Scenario: {scenario['input_dir']} ---")
        summary = batch_transcriber.batch_transcribe(**scenario)
        print(f"Batch Summary: {summary}")

if __name__ == '__main__':
    main()
