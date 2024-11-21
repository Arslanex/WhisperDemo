import os
import json
from pathlib import Path
from typing import Dict, Any, Union

class OutputHandler:
    """
    Advanced output handler for Whisper transcription results.
    Supports multiple output formats and advanced formatting options.
    """
    
    def __init__(self, output_dir: str = "transcriptions"):
        """
        Initialize the output handler.
        
        Args:
            output_dir (str, optional): Directory to save output files. Defaults to "transcriptions".
        """
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    @staticmethod
    def _format_timestamp(seconds: float, vtt: bool = False) -> str:
        """
        Convert seconds to timestamp format.
        
        Args:
            seconds (float): Time in seconds.
            vtt (bool, optional): Whether to use VTT timestamp format. Defaults to False.
        
        Returns:
            str: Formatted timestamp.
        """
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        secs = seconds % 60
        
        if vtt:
            return f"{hours:02d}:{minutes:02d}:{secs:06.3f}"
        else:
            return f"{hours:02d}:{minutes:02d}:{secs:06.3f}".replace(".", ",")

    def _format_srt(self, result: Dict[str, Any], include_word_timestamps: bool = False) -> str:
        """
        Format result as SRT subtitle file with improved time segmentation.
        
        Args:
            result (Dict[str, Any]): Transcription result.
            include_word_timestamps (bool, optional): Include word-level timestamps. Defaults to False.
        
        Returns:
            str: Formatted SRT content.
        """
        segments = result.get('segments', [])
        srt_content = []
        
        for i, segment in enumerate(segments, 1):
            start = self._format_timestamp(segment['start'])
            end = self._format_timestamp(segment['end'])
            text = segment['text'].strip()
            
            # Break long segments into shorter, more readable subtitles
            max_length = 50  # Maximum characters per subtitle line
            words = text.split()
            lines = []
            current_line = []
            current_length = 0
            
            for word in words:
                if current_length + len(word) > max_length:
                    lines.append(" ".join(current_line))
                    current_line = [word]
                    current_length = len(word)
                else:
                    current_line.append(word)
                    current_length += len(word) + 1
            
            if current_line:
                lines.append(" ".join(current_line))
            
            # Create subtitle with potentially multiple lines
            subtitle_text = "\n".join(lines)
            
            # Add word-level timestamps if requested
            if include_word_timestamps and 'words' in segment:
                word_timestamps = []
                for word_info in segment['words']:
                    word_start = self._format_timestamp(word_info['start'])
                    word_end = self._format_timestamp(word_info['end'])
                    word_timestamps.append(f"{word_start} --> {word_end}: {word_info['word']}")
                subtitle_text += "\n\n[Word Timestamps]\n" + "\n".join(word_timestamps)
            
            srt_content.extend([
                str(i),
                f"{start} --> {end}",
                subtitle_text,
                ""
            ])
        
        return "\n".join(srt_content)

    def _format_vtt(self, result: Dict[str, Any], include_word_timestamps: bool = False) -> str:
        """
        Format result as WebVTT subtitle file with improved time segmentation.
        
        Args:
            result (Dict[str, Any]): Transcription result.
            include_word_timestamps (bool, optional): Include word-level timestamps. Defaults to False.
        
        Returns:
            str: Formatted VTT content.
        """
        segments = result.get('segments', [])
        vtt_content = ["WEBVTT\n"]
        
        for segment in segments:
            start = self._format_timestamp(segment['start'], vtt=True)
            end = self._format_timestamp(segment['end'], vtt=True)
            text = segment['text'].strip()
            
            # Break long segments into shorter, more readable subtitles
            max_length = 50  # Maximum characters per subtitle line
            words = text.split()
            lines = []
            current_line = []
            current_length = 0
            
            for word in words:
                if current_length + len(word) > max_length:
                    lines.append(" ".join(current_line))
                    current_line = [word]
                    current_length = len(word)
                else:
                    current_line.append(word)
                    current_length += len(word) + 1
            
            if current_line:
                lines.append(" ".join(current_line))
            
            # Create subtitle with potentially multiple lines
            subtitle_text = "\n".join(lines)
            
            # Add word-level timestamps if requested
            if include_word_timestamps and 'words' in segment:
                word_timestamps = []
                for word_info in segment['words']:
                    word_start = self._format_timestamp(word_info['start'], vtt=True)
                    word_end = self._format_timestamp(word_info['end'], vtt=True)
                    word_timestamps.append(f"{word_start} --> {word_end}: {word_info['word']}")
                subtitle_text += "\n\n[Word Timestamps]\n" + "\n".join(word_timestamps)
            
            vtt_content.extend([
                f"{start} --> {end}",
                subtitle_text,
                ""
            ])
        
        return "\n".join(vtt_content)

    def format_output(self, result: Dict[str, Any], format: str) -> str:
        """
        Format transcription result according to specified format.
        
        Args:
            result (Dict[str, Any]): Transcription result.
            format (str): Output format (txt, json, srt, vtt).
        
        Returns:
            str: Formatted output.
        
        Raises:
            ValueError: If an unsupported output format is specified.
        """
        # Check if word timestamps are available
        include_word_timestamps = any('words' in segment for segment in result.get('segments', []))
        
        if format == "txt":
            return result['text']
        elif format == "json":
            return json.dumps(result, indent=2, ensure_ascii=False)
        elif format == "srt":
            return self._format_srt(result, include_word_timestamps)
        elif format == "vtt":
            return self._format_vtt(result, include_word_timestamps)
        else:
            raise ValueError(f"Unsupported output format: {format}")

    def save_output(self, result: Dict[str, Any], filename: str, format: str) -> str:
        """
        Save transcription result to file.
        
        Args:
            result (Dict[str, Any]): Transcription result.
            filename (str): Original filename.
            format (str): Output format.
        
        Returns:
            str: Path to the saved output file.
        """
        output_path = self.output_dir / f"{Path(filename).stem}.{format}"
        formatted_output = self.format_output(result, format)
        
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(formatted_output)
        
        return str(output_path)
