# 🧠 Sosyal Medya Yorumlarından Duygu Analizi  
Yapay Sinir Ağları Kullanılarak Youtube Yorumlarının Duygu Sınıflandırması

Belirli bir sosyal medya platformundan (YouTube) toplanan kullanıcı yorumlarını analiz ederek, bu yorumların duygu durumlarını (olumlu, olumsuz, nötr) sınıflandıran bir yapay zeka projesidir.
 
> 🎓 Proje, “Yapay Zeka Teknikleri” dersi vize ödevi kapsamında hazırlanmıştır.  

---

## ✨ Özellikler

🗃️ YouTube videolarından yorum çekme (Web Scraping – Selenium)  
🧪 LSTM tabanlı derin öğrenme ile duygu analizi  
🔤 Türkçe dil desteği ve doğal dil işleme teknikleri (NLP)  
📊 Eğitim/test doğruluklarının ve karışıklık matrisinin görselleştirilmesi  
🧾 Etiketli yorumlarla 3 sınıflı sınıflandırma (Pozitif, Negatif, Nötr)  
🖥️ Tkinter ile kullanıcı arayüzü (URL girerek yorum çekme)

---

## 📦 Kullanılan Teknolojiler

- 🐍 **Python** – Veri işleme, modelleme ve arayüz  
- 🧠 **Keras & TensorFlow** – LSTM tabanlı duygu analizi modeli  
- 🔤 **NLTK & Gensim** – Doğal dil işleme ve Word2Vec gömme  
- 🧪 **scikit-learn** – Model değerlendirme ve metrikler  
- 🌐 **Selenium** – YouTube’dan yorum çekme (Web scraping)  
- 🖼️ **Matplotlib & Seaborn** – Görselleştirme  
- 🎛️ **Tkinter** – Basit GUI arayüzü

---

## 📈 Model Yapısı
Gömme Katmanı (Word2Vec) – 300 boyutlu vektörler
LSTM Katmanı – 128 nöron
Dropout – 0.5 oranlı overfitting önleme
Global Max Pooling
Dense Katman – ReLU aktivasyonu
Çıkış Katmanı – 3 sınıflı softmax
   Model Adam optimizer ve EarlyStopping stratejisi ile eğitilmiştir.

---

## 📊 Performans Sonuçları
| Özellik          | Başlangıç Modeli | Geliştirilmiş Model |
| ---------------- | ---------------- | ------------------- |
| Eğitim Doğruluğu | %80              | %95                 |
| Test Doğruluğu   | %70              | %92                 |
| Epoch Sayısı     | 10               | 5-7 (EarlyStopping) |
| Overfitting      | Yüksek           | Düşük               |

---

## 🛠️ Kurulum ve Çalıştırma

1. Gerekli kütüphaneleri kurun:
   ```bash
   pip install pandas nltk scikit-learn keras gensim numpy matplotlib seaborn selenium webdriver-manager
2. Python dosyasını çalıştırın:
   python web_scraping_arayüz.py
3. Açılan pencerede YouTube video URL'sini girin ve yorumları analiz edin.

---

## 🔧 Uygulama arayüzü ve işlevi görselleri için result_images dosyasını inceleyin!
