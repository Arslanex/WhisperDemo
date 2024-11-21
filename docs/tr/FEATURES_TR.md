# Whisper Transkripsiyon Modülü - Özellik Spesifikasyonları

## 1. Temel Transkripsiyon Yetenekleri

### 1.1 Model Desteği
- Tüm Whisper model boyutlarını destekler:
  - `tiny`: En küçük, en hızlı, en az doğru
  - `base`: Hızlı, dengeli performans
  - `small`: İyi doğruluk, orta düzey kaynak kullanımı
  - `medium`: Yüksek doğruluk, çoğu kullanım için önerilen
  - `large`: En doğru, en yüksek kaynak gereksinimleri

### 1.2 Transkripsiyon Modları
- **Transkripsiyon**: Konuşmayı orijinal dilde metne dönüştürme
- **Çeviri**: Konuşmayı İngilizceye çevirme
- Otomatik dil algılama
- Manuel dil belirtme

## 2. Gelişmiş Yapılandırma Seçenekleri

### 2.1 Kalite Kontrol Parametreleri
- **Sıcaklık Örneklemesi**
  - Çeşitli transkripsiyon denemeleri için birden fazla sıcaklık değeri
  - Transkripsiyon doğruluğunu artırmaya yardımcı olur
  - Varsayılan: 0.0 (deterministik)
  - Aralık: 0.0 - 1.0

- **Sıkıştırma Oranı Eşiği**
  - Yüksek sıkıştırma oranına sahip segmentleri filtrele
  - Düşük kaliteli veya gürültülü segmentleri gösterir
  - Varsayılan: 2.4

- **Log Olasılık Eşiği**
  - Düşük log olasılığına sahip segmentleri kaldır
  - Belirsiz transkripsiyon parçalarını filtrelemeye yardımcı olur
  - Varsayılan: -1.0

- **Konuşma Dışı Eşik**
  - Konuşma dışı segmentleri algıla ve filtrele
  - Arka plan gürültüsünü kaldırmak için kullanışlı
  - Varsayılan: 0.6

### 2.2 Segment Filtreleme
- **Maksimum Segment Uzunluğu**
  - Uzun transkripsiyon parçalarını okunabilir segmentlere böl
  - Yapılandırılabilir karakter sınırı
  - Varsayılan: 50 karakter

- **Minimum Segment Uzunluğu**
  - Çok kısa, muhtemelen ilgisiz segmentleri yoksay
  - Yapılandırılabilir karakter sınırı
  - Varsayılan: 10 karakter

## 3. Çıktı Formatlandırma

### 3.1 Desteklenen Formatlar
- Düz Metin (`.txt`)
- SubRip Altyazı (`.srt`)
- WebVTT Altyazı (`.vtt`)
- JSON (`.json`)

### 3.2 Kelime Düzeyinde Zaman Damgaları
- Her kelime için kesin zamanlama
- Destekler:
  - Başlangıç zamanı
  - Bitiş zamanı
  - Kelime metni

### 3.3 Altyazı Özellikleri
- Yapılandırılabilir altyazı formatlandırma
- Otomatik satır sonları
- Zaman damgası hassasiyeti

## 4. Performans Değerlendirmesi

### 4.1 Hesaplama Kaynakları
- **CPU Desteği**: Tüm modeller
- **GPU İvmelendirme**: İsteğe bağlı, performansı artırır
- Kaynak kullanımı model boyutuyla ölçeklenir

### 4.2 Ses Girdi Desteği
- Birden fazla ses formatını destekler
- Ses işleme için `ffmpeg`'e dayanır
- Önerilen formatlar: 
  - WAV
  - MP3
  - M4A
  - FLAC

## 5. Hata Yönetimi ve Günlük Kaydı

### 5.1 Ayrıntılı Mod
- Transkripsiyon sürecinin detaylı günlük kaydı
- Transkripsiyon sorunlarını tanılamaya yardımcı olur
- Yapılandırılabilir ayrıntılılık seviyeleri

### 5.2 Ele Alınan Hata Türleri
- Desteklenmeyen ses formatları
- Yetersiz hesaplama kaynakları
- Dil algılama hataları
- Transkripsiyon kalite sorunları

## 6. Genişletilebilirlik

### 6.1 Özelleştirme Noktaları
- Özel başlangıç ipuçları
- Dile özgü ayarlama
- Esnek yapılandırma seçenekleri

### 6.2 Gelecek Yol Haritası
- Gelişmiş dil desteği
- Daha gelişmiş filtreleme
- İyileştirilmiş çeviri yetenekleri
- Makine öğrenimi model güncellemeleri

## 7. Uyumluluk

### 7.1 Python Sürümleri
- Python 3.8+
- Başlıca işletim sistemlerinde test edilmiştir
  - macOS
  - Linux
  - Windows

### 7.2 Bağımlılıklar
- `openai-whisper`
- `torch`
- `numpy`
- `soundfile`
- `ffmpeg-python`

## 8. Lisanslama ve Atıf
- OpenAI Whisper modelini kullanır
- Whisper model lisanslamasını izler
- Açık kaynak uygulama

## 9. En İyi Uygulamalar
- Kullanım durumunuz için uygun model boyutunu kullanın
- Yüksek kaliteli ses girişi sağlayın
- Yapılandırma seçenekleriyle deney yapın
- Transkripsiyon kalitesini izleyin
