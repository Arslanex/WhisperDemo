import os
import argparse
from pathlib import Path
from typing import Dict, Any, Optional, Union, List

import torch
import whisper
import soundfile as sf
import numpy as np

from .config import TranscriptionConfig
from .output_handler import OutputHandler

class WhisperTranscriber:
    """Advanced Whisper transcription class with extended capabilities."""
    
    def __init__(self, config: Optional[TranscriptionConfig] = None):
        """
        Initialize the transcriber with advanced configuration options.
        
        Args:
            config (Optional[TranscriptionConfig]): Configuration for transcription.
        """
        self.config = config or TranscriptionConfig()
        self.config.validate()
        
        # Load model with device specification
        if self.config.device == "cuda" and not torch.cuda.is_available():
            print("CUDA not available. Falling back to CPU.")
            self.config.device = "cpu"
        
        self.model = whisper.load_model(
            self.config.model_name, 
            device=self.config.device
        )
        self.output_handler = OutputHandler(self.config.output_dir)

    def _filter_segments(self, segments: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Apply advanced filtering to transcription segments.
        
        Args:
            segments (List[Dict[str, Any]]): Original transcription segments.
        
        Returns:
            List[Dict[str, Any]]: Filtered transcription segments.
        """
        filtered_segments = []
        
        for segment in segments:
            text = segment.get('text', '').strip()
            
            # Apply minimum segment length filter
            if (self.config.min_segment_length is not None and 
                len(text) < self.config.min_segment_length):
                continue
            
            # Apply maximum segment length filter
            if (self.config.max_segment_length is not None and 
                len(text) > self.config.max_segment_length):
                # Split long segments
                words = text.split()
                for i in range(0, len(words), self.config.max_segment_length):
                    chunk = ' '.join(words[i:i+self.config.max_segment_length])
                    chunk_segment = segment.copy()
                    chunk_segment['text'] = chunk
                    filtered_segments.append(chunk_segment)
                continue
            
            filtered_segments.append(segment)
        
        return filtered_segments

    def transcribe(self, audio_path: Union[str, Path]) -> Dict[str, Any]:
        """
        Transcribe audio file using Whisper with extended options.
        
        Args:
            audio_path (Union[str, Path]): Path to the audio file.
        
        Returns:
            Dict[str, Any]: Transcription result with optional word-level timestamps.
        """
        audio_path = Path(audio_path)
        
        if not audio_path.exists():
            raise FileNotFoundError(f"Audio file not found: {audio_path}")
        
        # Validate audio file
        try:
            sf.info(str(audio_path))
        except Exception as e:
            raise ValueError(f"Invalid audio file: {e}")
        
        # Prepare transcription options
        transcribe_options = {
            "language": self.config.language,
            "task": self.config.task,
            "verbose": self.config.verbose,
            "temperature": self.config.temperature,
            "compression_ratio_threshold": self.config.compression_ratio_threshold,
            "logprob_threshold": self.config.logprob_threshold,
            "no_speech_threshold": self.config.no_speech_threshold,
            "condition_on_previous_text": self.config.condition_on_previous_text,
            "initial_prompt": self.config.initial_prompt,
            "word_timestamps": self.config.word_timestamps,
            "prepend_punctuations": self.config.prepend_punctuations,
            "append_punctuations": self.config.append_punctuations,
            "clip_timestamps": self.config.clip_timestamps,
            "hallucination_silence_threshold": self.config.hallucination_silence_threshold
        }
        
        # Remove None values
        transcribe_options = {k: v for k, v in transcribe_options.items() if v is not None}
        
        # Perform transcription
        result = self.model.transcribe(
            str(audio_path),
            **transcribe_options
        )
        
        # Apply segment filtering if configured
        if self.config.min_segment_length or self.config.max_segment_length:
            result['segments'] = self._filter_segments(result.get('segments', []))
        
        return result

    def process_file(self, audio_path: Union[str, Path]) -> str:
        """
        Process a single audio file and save the result.
        
        Args:
            audio_path (Union[str, Path]): Path to the audio file.
        
        Returns:
            str: Path to the saved output file.
        """
        result = self.transcribe(audio_path)
        output_path = self.output_handler.save_output(
            result,
            str(audio_path),
            self.config.output_format
        )
        return output_path

    def process_directory(self, directory: Union[str, Path]) -> Dict[str, str]:
        """
        Process all audio files in a directory.
        
        Args:
            directory (Union[str, Path]): Path to the directory.
        
        Returns:
            Dict[str, str]: Mapping of input files to output files.
        """
        directory = Path(directory)
        if not directory.is_dir():
            raise NotADirectoryError(f"Directory not found: {directory}")
        
        results = {}
        audio_extensions = {".wav", ".mp3", ".m4a", ".flac", ".ogg"}
        
        for file_path in directory.rglob("*"):
            if file_path.suffix.lower() in audio_extensions:
                try:
                    output_path = self.process_file(file_path)
                    results[str(file_path)] = output_path
                except Exception as e:
                    results[str(file_path)] = f"Error: {str(e)}"
        
        return results

def main():
    """Command-line interface for the transcriber with extended options."""
    parser = argparse.ArgumentParser(description="Advanced Whisper Audio Transcription Tool")
    
    # Basic arguments
    parser.add_argument("input_path", help="Path to audio file or directory")
    parser.add_argument("--model", default="base", help="Whisper model to use")
    parser.add_argument("--language", help="Language of the audio (optional)")
    parser.add_argument("--task", default="transcribe", choices=["transcribe", "translate"],
                      help="Task to perform (transcribe or translate)")
    parser.add_argument("--device", default="cpu", choices=["cpu", "cuda"],
                      help="Device to use for computation")
    parser.add_argument("--output-dir", default="transcriptions",
                      help="Directory to save output files")
    parser.add_argument("--format", default="srt", choices=["txt", "json", "srt", "vtt"],
                      help="Output format")
    
    # Advanced Whisper options
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    parser.add_argument("--temperature", type=float, nargs="+", default=[0.0, 0.2, 0.4, 0.6, 0.8, 1.0],
                      help="Sampling temperatures for decoding")
    parser.add_argument("--compression-ratio-threshold", type=float, default=2.4,
                      help="Compression ratio threshold for filtering")
    parser.add_argument("--logprob-threshold", type=float, default=-1.0,
                      help="Log probability threshold for filtering")
    parser.add_argument("--no-speech-threshold", type=float, default=0.6,
                      help="No speech threshold for filtering")
    parser.add_argument("--word-timestamps", action="store_true",
                      help="Enable word-level timestamps")
    parser.add_argument("--initial-prompt", help="Initial text prompt for transcription")
    parser.add_argument("--max-segment-length", type=int,
                      help="Maximum length of transcription segments")
    parser.add_argument("--min-segment-length", type=int,
                      help="Minimum length of transcription segments")
    
    args = parser.parse_args()
    
    config = TranscriptionConfig(
        model_name=args.model,
        language=args.language,
        task=args.task,
        device=args.device,
        output_dir=args.output_dir,
        output_format=args.format,
        verbose=args.verbose,
        temperature=tuple(args.temperature),
        compression_ratio_threshold=args.compression_ratio_threshold,
        logprob_threshold=args.logprob_threshold,
        no_speech_threshold=args.no_speech_threshold,
        word_timestamps=args.word_timestamps,
        initial_prompt=args.initial_prompt,
        max_segment_length=args.max_segment_length,
        min_segment_length=args.min_segment_length
    )
    
    transcriber = WhisperTranscriber(config)
    input_path = Path(args.input_path)
    
    try:
        if input_path.is_file():
            output_path = transcriber.process_file(input_path)
            print(f"Transcription saved to: {output_path}")
        elif input_path.is_dir():
            results = transcriber.process_directory(input_path)
            print("\nTranscription Results:")
            for input_file, output_file in results.items():
                print(f"\n{input_file} -> {output_file}")
        else:
            print(f"Error: Path not found: {input_path}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
