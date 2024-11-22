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
from whisper_transcriber import WhisperTranscriber, TranscriptionConfig

# Yapılandırma oluştur
config = TranscriptionConfig(
    model_name='base',           # Kullanılacak Whisper modeli
    verbose=False           # Ayrıntılı çıktıyı devre dışı bırak
)

# Transkriber'ı başlat
transcriber = WhisperTranscriber(config)

# Ses dosyasını dökümleştir
result = transcriber.transcribe('path/to/audio.mp3')

# Transkripsiyon sonuçlarını al
print(result.text)  # Tam transkripsiyon metni
print(result.segments)  # Detaylı segment bilgileri
```

## Gelişmiş Yapılandırma

### Detaylı Transkripsiyon Seçenekleri
```python
config = TranscriptionConfig(
    # Model Seçimi
    model_name='medium',         # Seçenekler: tiny, base, small, medium, large
    task='transcribe',      # 'transcribe' veya 'translate'
    
    # Kalite Kontrol
    temperature=[0.0, 0.2],  # Birden fazla örnekleme sıcaklığı
    compression_ratio_threshold=2.4,
    logprob_threshold=-1.0,
    no_speech_threshold=0.6,
    
    # Segment Filtreleme
    max_segment_length=50,  # Segment başına maksimum karakter
    min_segment_length=10,  # Segment başına minimum karakter
    
    # Çıktı Formatlandırma
    word_timestamps=True,   # Kelime düzeyinde zamanlama
    verbose=True            # Detaylı günlük kaydı
)
```

### Çıktı İşleme
```python
# Birden fazla çıktı formatı oluştur
transcriber.generate_outputs(
    result, 
    output_dir='./transkriptler',
    formats=['srt', 'txt', 'json']
)
```

## Gelişmiş Özellikler

### Dil Algılama
```python
# Otomatik dil algılama
config = TranscriptionConfig(language=None)  # Otomatik algıla
```

### Çeviri Modu
```python
config = TranscriptionConfig(
    task='translate',       # İngilizceye çevir
    model_name='medium'          # Çeviri için önerilen model
)
```

## Hata Yönetimi
```python
try:
    result = transcriber.transcribe('audio.mp3')
except Exception as e:
    print(f"Transkripsiyon hatası: {e}")
```

## Performans Değerlendirmesi
- Büyük modeller daha iyi doğruluk sağlar ancak daha fazla hesaplama kaynağı gerektirir
- CPU ve GPU performansı değişkenlik gösterir
- Hızlı transkripsiyon için küçük modeller önerilir
- Büyük modeller yüksek doğruluk gerektiren durumlar için idealdir

## Günlük Kaydı ve Hata Ayıklama
```python
config = TranscriptionConfig(verbose=True)
# Transkripsiyon sürecinin detaylı günlük kaydını etkinleştirir
```

## Notlar
- Ses işleme için `ffmpeg`'in kurulu olduğundan emin olun
- Bazı özellikler ek bağımlılıklar gerektirebilir
- Performans ses kalitesi, model boyutu ve sistem kaynaklarına bağlıdır
