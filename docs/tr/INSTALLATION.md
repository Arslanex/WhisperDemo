# Whisper Transcriber - Kurulum Kılavuzu

## Ön Gereksinimler
- Python 3.8 veya üzeri
- pip (Python paket yöneticisi)
- İşletim Sistemi: macOS, Linux veya Windows
- Önerilen: Sanal ortam (Virtual environment)

## Kurulum Yöntemleri

### 1. Paket Olarak Kurulum (Önerilen)

#### pip Kullanarak
```bash
# En son kararlı sürümü yükle
pip install whisper-transcriber

# Belirli bir sürümü yükle
pip install whisper-transcriber==X.X.X
```

#### Sanal Ortam (Önerilen)
```bash
# Sanal ortam oluştur
python3 -m venv whisper-env

# Sanal ortamı etkinleştir
# macOS/Linux için
source whisper-env/bin/activate
# Windows için
whisper-env\Scripts\activate

# Sanal ortama paketi yükle
pip install whisper-transcriber
```

### 2. Git Deposundan Kurulum

#### Depoyu Klonlama
```bash
# Depoyu klonla
git clone https://github.com/your-org/whisper-transcriber.git

# Proje dizinine git
cd whisper-transcriber

# Düzenlenebilir modda yükle
pip install -e .
```

### 3. Bağımlılıkları Yükleme

#### Temel Bağımlılıklar
```bash
# Temel bağımlılıkları manuel olarak yükle
pip install torch
pip install openai-whisper
pip install soundfile
pip install numpy
pip install typing-extensions
```

#### İsteğe Bağlı Bağımlılıklar
```bash
# GPU Desteği (CUDA)
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

# Ek ses işleme kitaplıkları
pip install librosa
```

### 4. FFmpeg Kurulumu

#### macOS (Homebrew)
```bash
# Homebrew'ı yükle (zaten yüklü değilse)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# FFmpeg'i yükle
brew install ffmpeg
```

#### Linux (Ubuntu/Debian)
```bash
# Paket listesini güncelle
sudo apt update

# FFmpeg'i yükle
sudo apt install ffmpeg
```

#### Linux (Fedora)
```bash
# FFmpeg'i yükle
sudo dnf install ffmpeg
```

#### Windows
1. FFmpeg'i resmi web sitesinden indirin: https://ffmpeg.org/download.html
2. ZIP dosyasını çıkartın
3. `bin` dizinini sistem PATH'ine ekleyin

### 5. Kurulumu Doğrulama

```bash
# Whisper Transcriber kurulumunu doğrula
pip show whisper-transcriber

# Temel işlevselliği test et
whisper-transcribe --help
```

## Sorun Giderme

### Yaygın Kurulum Sorunları
- Python sürümünün uyumlu olduğundan emin olun
- pip'in güncel olduğunu kontrol edin: `pip install --upgrade pip`
- Tüm bağımlılıkların doğru yüklendiğini doğrulayın
- GPU desteği için CUDA araç setinin yüklü olduğundan emin olun

### Performans Değerlendirmeleri
- Daha büyük Whisper modelleri daha fazla hesaplama kaynağı gerektirir
- Büyük ses dosyaları için GPU hızlandırması önerilir
- Donanım yeteneklerinize göre model boyutunu seçin

## Önerilen Sistem Gereksinimleri

### Minimum
- CPU: Intel Core i5 veya eşdeğeri
- RAM: 8 GB
- Disk Alanı: 1 GB (küçük Whisper modelleri için)

### Önerilen
- CPU: Intel Core i7 veya AMD Ryzen 7
- RAM: 16 GB
- GPU: CUDA destekli NVIDIA
- Disk Alanı: 5 GB (büyük Whisper modelleri için)

## Notlar
- Her zaman sanal ortam kullanın
- Bağımlılıkları güncel tutun
- En son kurulum talimatları için proje belgelerini kontrol edin
