# Whisper Transcriber - Komut Satırı Arayüzü (CLI) Kullanım Kılavuzu

## Genel Bakış
Whisper Transcriber CLI, ses dosyalarını doğrudan komut satırından dökümante etmek için güçlü ve kullanıcı dostu bir arabirim sağlar.

## Kurulum
```bash
pip install whisper-transcriber
```

## Temel Kullanım

### Basit Transkripsiyon
```bash
# Ses dosyasının temel dökümantasyonu
whisper-transcribe ses_dosyasi.mp3

# Çıktı dizinini belirtme
whisper-transcribe ses_dosyasi.mp3 --output-dir ./transkriptler
```

## Gelişmiş Kullanım

### Model ve Dil Seçimi
```bash
# Belirli Whisper modelini seçme
whisper-transcribe ses_dosyasi.mp3 --model medium

# Kaynak dili belirtme
whisper-transcribe ses_dosyasi.mp3 --language tr

# İngilizceye çevirme
whisper-transcribe ses_dosyasi.mp3 --task translate
```

## Çıktı Formatları

### Birden Fazla Çıktı Formatı
```bash
# Birden fazla çıktı formatı oluşturma
whisper-transcribe ses_dosyasi.mp3 --output-format srt txt json

# Özel çıktı dizini belirtme
whisper-transcribe ses_dosyasi.mp3 --output-dir ./transkriptler --output-format vtt
```

## Toplu İşleme

### Birden Fazla Dosyayı Dökümante Etme
```bash
# Bir dizindeki tüm ses dosyalarını dökümante etme
whisper-transcribe /ses/dizini/* --recursive

# Belirli bir model ile toplu işlem
whisper-transcribe /ses/dizini/* --model small --recursive
```

## Performans ve Kalite Kontrolü

### Gelişmiş Yapılandırma
```bash
# Transkripsiyon kalitesini kontrol etme
whisper-transcribe ses_dosyasi.mp3 \
    --temperature 0.0 0.2 \
    --compression-ratio-threshold 2.4 \
    --logprob-threshold -1.0 \
    --no-speech-threshold 0.6

# Segment uzunluğunu kontrol etme
whisper-transcribe ses_dosyasi.mp3 \
    --max-segment-length 50 \
    --min-segment-length 10
```

## Günlük Kaydı ve Hata Ayıklama

### Ayrıntılı Çıktı
```bash
# Detaylı günlük kaydını etkinleştirme
whisper-transcribe ses_dosyasi.mp3 --verbose

# Günlük dosyasına kaydetme
whisper-transcribe ses_dosyasi.mp3 --verbose --log-file transkripsiyon.log
```

## GPU ve Performans

### GPU Hızlandırma
```bash
# Daha hızlı işleme için GPU kullanma
whisper-transcribe ses_dosyasi.mp3 --device cuda

# Belirli GPU cihazını seçme
whisper-transcribe ses_dosyasi.mp3 --device cuda:0
```

## Yaygın Seçenekler

### Tam Komut Referansı
```bash
whisper-transcribe [SEÇENEKLER] GİRDİ_DOSYASI

Seçenekler:
  --model TEXT            Kullanılacak Whisper modeli (tiny/base/small/medium/large)
  --task TEXT             Transkripsiyon görevi (transcribe/translate)
  --language TEXT         Kaynak dil kodu
  --output-dir TEXT       Transkripsiyon dosyaları için çıktı dizini
  --output-format TEXT    Çıktı dosya formatları (txt/srt/json/vtt)
  --device TEXT           İşleme cihazı (cpu/cuda)
  --verbose              Detaylı günlük kaydını etkinleştir
  --log-file TEXT         Günlük dosyası yolu
  --temperature FLOAT    Örnekleme sıcaklığı
  --max-segment-length INT Maksimum segment uzunluğu
  --min-segment-length INT Minimum segment uzunluğu
  --recursive            Dizindeki tüm dosyaları işle
  --help                 Bu yardım mesajını göster
```

## Örnekler

### Gerçek Dünya Senaryoları
```bash
# Podcast bölümünü dökümante etme
whisper-transcribe podcast.mp3 --model medium --language tr --output-format srt txt

# Yabancı dilde videoyu çevirme
whisper-transcribe yabanci_video.mp4 --task translate --model large

# Röportaj kayıtlarını toplu işleme
whisper-transcribe /röportaj/dizini/* --recursive --model small
```

## Sorun Giderme

### Sık Karşılaşılan Sorunlar
- `ffmpeg`'in yüklü olduğundan emin olun
- Ses dosyası formatını ve kalitesini kontrol edin
- Yeterli disk alanı olduğunu doğrulayın
- Donanımınıza uygun modeli kullanın

## Performans İpuçları
- Daha küçük modeller daha hızlıdır ancak daha az doğrudur
- Büyük dosyalar için GPU kullanın
- Transkripsiyon öncesi ses kalitesini doğrulayın

## Sınırlamalar
- Transkripsiyon doğruluğu şunlara bağlıdır:
  - Model boyutu
  - Ses kalitesi
  - Arka plan gürültüsü
  - Konuşmacı netliği
- Büyük dosyalar daha fazla işleme süresi gerektirebilir
- Bazı aksanlar doğruluğu düşürebilir

## Notlar
- Çoğu ses ve video formatını destekler
- Python 3.8+ gerektirir
- Büyük dosyalar için GPU hızlandırması önerilir
