# Whisper Transkripsiyon Modülü - Komut Satırı Kullanımı

## Genel Bakış
Whisper Transkripsiyon Modülü, gelişmiş yapılandırma seçenekleriyle ses dosyalarını dökümleştirmek için güçlü bir komut satırı arayüzü sağlar.

## Temel Kullanım
```bash
python -m whisper_transcriber [SEÇENEKLER] GİRDİ_DOSYASI
```

## Komut Satırı Seçenekleri

### Temel Transkripsiyon Seçenekleri
- `GİRDİ_DOSYASI`: Dökümlenecek ses dosyasının yolu (zorunlu)
- `-o, --output-dir`: Transkripsiyon dosyalarını kaydetme dizini (varsayılan: geçerli dizin)
- `-m, --model`: Kullanılacak Whisper modeli (varsayılan: 'base')
  - Seçenekler: 'tiny', 'base', 'small', 'medium', 'large'

### Gelişmiş Transkripsiyon Yapılandırması
- `--language`: Ses dilini belirle (opsiyonel, belirtilmezse otomatik algıla)
- `--task`: Transkripsiyon görev türü (varsayılan: 'transcribe')
  - Seçenekler: 'transcribe', 'translate'
- `--verbose`: Ayrıntılı çıktıyı etkinleştir
- `--temperature`: Transkripsiyon için örnekleme sıcaklığı (varsayılan: 0.0)
  - Birden fazla sıcaklık belirtilebilir: `--temperature 0.0 0.2 0.4`

### Filtreleme ve Kalite Kontrol Seçenekleri
- `--compression-ratio-threshold`: İzin verilen maksimum sıkıştırma oranı
- `--log-prob-threshold`: Segment dahil etme için minimum log olasılığı
- `--no-speech-threshold`: Konuşma dışı segmentleri algılama eşiği
- `--max-segment-length`: Transkripsiyon segment uzunluğu üst sınırı
- `--min-segment-length`: Transkripsiyon segment uzunluğu alt sınırı

### Çıktı Formatı Seçenekleri
- `--output-formats`: Çıktı dosya formatlarını belirle
  - Seçenekler: 'txt', 'srt', 'vtt', 'json'
  - Örnek: `--output-formats srt txt`
- `--word-timestamps`: Kelime düzeyinde zaman damgalarını etkinleştir

## Örnekler

### Temel Transkripsiyon
```bash
python -m whisper_transcriber audio.mp3
```

### Çoklu Seçeneklerle Gelişmiş Transkripsiyon
```bash
python -m whisper_transcriber audio.mp3 \
    --model medium \
    --language tr \
    --output-dir ./transkriptler \
    --output-formats srt txt \
    --word-timestamps \
    --temperature 0.0 0.2 \
    --max-segment-length 50
```

## Notlar
- Gerekli bağımlılıkların kurulu olduğundan emin olun
- Büyük modeller önemli hesaplama kaynakları gerektirebilir
- Performans ses kalitesi ve model boyutuna bağlıdır
