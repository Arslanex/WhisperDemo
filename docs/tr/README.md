# Whisper Transkripsiyon Modülü - Kurulum Kılavuzu

## 🚀 Kurulum Yöntemleri

### 1. Normal Kurulum
Modülü kullanmak isteyen çoğu kullanıcı için:

```bash
# PyPI'dan kur
pip install whisper-transcriber

# Veya yerel dizinden kur
pip install .
```

#### Normal Kurulum Ne Zaman Kullanılır:
- Projenizde modülü kullanmak istiyorsunuz
- Son kullanıcısınız
- Paket kaynak kodunu değiştirmeyi planlamıyorsunuz

### 2. Düzenlenebilir (Geliştirme) Kurulum
Geliştiriciler ve katkıda bulunanlar için:

```bash
# Düzenlenebilir modda kur
pip install -e .
```

#### Düzenlenebilir Kurulum Ne Zaman Kullanılır:
- Paketi geliştiriyorsunuz
- Sık sık kod değişiklikleri yapmak istiyorsunuz
- Yeniden yüklemeden değişiklikleri test etmeniz gerekiyor
- Paket geliştirmeye katkıda bulunuyorsunuz

### 3. Geliştirme Bağımlılıkları
Katkıda bulunuyorsanız veya testler çalıştırıyorsanız:

```bash
# Geliştirme bağımlılıkları ile kur
pip install -e .[dev]
```

## 📋 Gereksinimler
- Python 3.8+
- Bağımlılıklar:
  - openai-whisper
  - torch
  - numpy
  - soundfile
  - ffmpeg-python

## 🔍 Sorun Giderme
- En son pip sürümüne sahip olduğunuzdan emin olun
- Python sürüm uyumluluğunu kontrol edin
- Sistem bağımlılıklarını (ffmpeg) kurun

## 🤝 Katkıda Bulunma
- Depoyu çatallayın (fork)
- Sanal bir ortam oluşturun
- Düzenlenebilir kurulum kullanın
- PR göndermeden önce testleri çalıştırın
