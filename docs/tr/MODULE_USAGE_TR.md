# Whisper Transkripsiyon Modülü - Python Modül Kullanımı

## Genel Bakış
Whisper Transkripsiyon Modülü, Python betiklerinde doğrudan içe aktarılabilir ve kullanılabilir, esnek ve programatik ses dökümleştirmesi sağlar.

## Kurulum
```bash
pip install whisper-transcriber
```

## Temel Kullanım

### Basit Transkripsiyon
```python
from whisper_transcriber.transcriber import WhisperTranscriber
from whisper_transcriber.config import TranscriptionConfig

# Yapılandırma oluştur
transcription_config = TranscriptionConfig(
    model_name='base',           # Kullanılacak Whisper modeli
    verbose=False                # Ayrıntılı çıktıyı devre dışı bırak
)

# Transkriber'ı başlat
whisper_transcriber = WhisperTranscriber(transcription_config)

# Ses dosyasını dökümleştir
transcription_result = whisper_transcriber.transcribe('path/to/audio.mp3')

# Transkripsiyon sonuçlarını al
print(transcription_result['text'])  # Tam transkripsiyon metni
print(transcription_result['segments'])  # Detaylı segment bilgileri
```

## Gelişmiş Yapılandırma

### Detaylı Transkripsiyon Seçenekleri
```python
advanced_config = TranscriptionConfig(
    # Model Seçimi
    model_name='medium',         # Seçenekler: tiny, base, small, medium, large
    task='transcribe',           # 'transcribe' veya 'translate'
    language='tr',               # Dil kodu (isteğe bağlı)
    
    # Kalite Kontrol
    temperature=(0.0, 0.2),      # Birden fazla örnekleme sıcaklığı
    compression_ratio_threshold=2.4,
    logprob_threshold=-1.0,
    no_speech_threshold=0.6,
    
    # Segment Filtreleme
    max_segment_length=50,       # Segment başına maksimum karakter
    min_segment_length=10,       # Segment başına minimum karakter
    
    # Çıktı Yapılandırması
    output_format='srt',         # Çıktı formatı: txt, json, srt, vtt
    output_dir='./transcriptions' # Çıktı dizini
)

# Gelişmiş transkripsiyon
advanced_transcriber = WhisperTranscriber(advanced_config)
advanced_result = advanced_transcriber.transcribe('path/to/long_audio.mp3')
```

## Toplu İşlem

### Dizindeki Tüm Ses Dosyalarını Dökümleştirme
```python
# Tüm ses dosyalarını dökümleştir
batch_config = TranscriptionConfig(
    model_name='small',
    task='transcribe'
)

batch_transcriber = WhisperTranscriber(batch_config)
batch_results = batch_transcriber.process_directory('/path/to/audio/directory')

# Sonuçları işle
for audio_path, output_path in batch_results.items():
    print(f"Audio: {audio_path}, Transcription: {output_path}")
```

## Hata Yakalama ve Günlükleme

### Hata İşleme Örneği
```python
try:
    transcription_result = whisper_transcriber.transcribe('problematic_audio.mp3')
except FileNotFoundError:
    print("Ses dosyası bulunamadı")
except ValueError as e:
    print(f"Dökümleştirme hatası: {e}")
```

## Performans İpuçları
- Küçük modeller daha hızlı, daha az doğru
- Büyük modeller daha yavaş, daha doğru
- GPU kullanımı işlemi hızlandırır
- Ses kalitesi transkripsiyon doğruluğunu etkiler

## Desteklenen Özellikler
- Çoklu model desteği
- Dil çevirisi
- Detaylı segment filtreleme
- Çeşitli çıktı formatları
- GPU ve CPU desteği
