from dataclasses import dataclass, field
from typing import Optional, Dict, Any, Union, List, Tuple

import whisper

@dataclass
class TranscriptionConfig:
    """Advanced configuration for Whisper transcription."""
    # Basic configuration
    model_name: str = "base"
    language: Optional[str] = None
    task: str = "transcribe"
    device: str = "cpu"
    output_dir: str = "transcriptions"
    output_format: str = "srt"

    # Advanced Whisper transcription options
    verbose: Optional[bool] = None
    temperature: Union[float, Tuple[float, ...]] = (0.0, 0.2, 0.4, 0.6, 0.8, 1.0)
    
    # Filtering and quality control options
    compression_ratio_threshold: Optional[float] = 2.4
    logprob_threshold: Optional[float] = -1.0
    no_speech_threshold: Optional[float] = 0.6
    
    # Text generation and formatting options
    condition_on_previous_text: bool = True
    initial_prompt: Optional[str] = None
    word_timestamps: bool = False
    
    # Punctuation and timestamp options
    prepend_punctuations: str = '"\'"¿([{-'
    append_punctuations: str = '"\'.。,，!！?？:：")]}、'
    clip_timestamps: Union[str, List[float]] = '0'
    hallucination_silence_threshold: Optional[float] = None
    
    # Additional filtering options
    max_segment_length: Optional[int] = None  # Maximum length of transcription segments
    min_segment_length: Optional[int] = None  # Minimum length of transcription segments
    
    def validate(self) -> None:
        """Validate configuration settings with extended checks."""
        # Existing validations
        valid_tasks = ["transcribe", "translate"]
        valid_devices = ["cpu", "cuda"]
        valid_formats = ["txt", "json", "srt", "vtt"]
        
        if self.task not in valid_tasks:
            raise ValueError(f"Task must be one of {valid_tasks}")
        
        if self.device not in valid_devices:
            raise ValueError(f"Device must be one of {valid_devices}")
            
        if self.output_format not in valid_formats:
            raise ValueError(f"Output format must be one of {valid_formats}")
        
        # Validate model
        try:
            whisper.load_model(self.model_name)
        except Exception as e:
            raise ValueError(f"Invalid model name: {self.model_name}") from e
        
        # Additional validations for new parameters
        if self.max_segment_length is not None and self.max_segment_length <= 0:
            raise ValueError("max_segment_length must be a positive integer")
        
        if self.min_segment_length is not None and self.min_segment_length <= 0:
            raise ValueError("min_segment_length must be a positive integer")
        
        if self.min_segment_length and self.max_segment_length:
            if self.min_segment_length > self.max_segment_length:
                raise ValueError("min_segment_length cannot be greater than max_segment_length")

    def to_dict(self) -> Dict[str, Any]:
        """Convert configuration to dictionary format with extended options."""
        return {
            "model_name": self.model_name,
            "language": self.language,
            "task": self.task,
            "device": self.device,
            "output_dir": self.output_dir,
            "output_format": self.output_format,
            "verbose": self.verbose,
            "temperature": self.temperature,
            "compression_ratio_threshold": self.compression_ratio_threshold,
            "logprob_threshold": self.logprob_threshold,
            "no_speech_threshold": self.no_speech_threshold,
            "condition_on_previous_text": self.condition_on_previous_text,
            "initial_prompt": self.initial_prompt,
            "word_timestamps": self.word_timestamps,
            "prepend_punctuations": self.prepend_punctuations,
            "append_punctuations": self.append_punctuations,
            "clip_timestamps": self.clip_timestamps,
            "hallucination_silence_threshold": self.hallucination_silence_threshold,
            "max_segment_length": self.max_segment_length,
            "min_segment_length": self.min_segment_length
        }

    @classmethod
    def from_dict(cls, config_dict: Dict[str, Any]) -> 'TranscriptionConfig':
        """Create configuration from dictionary with extended options."""
        return cls(**config_dict)
