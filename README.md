# 🫀 Heart Disease Prediction - Machine Learning Project

Bu proje, **kalp hastalığı veriseti** kullanılarak makine öğrenmesi modelleri ile hastalık tahmini yapılmasını amaçlar. Projede veri analizi, korelasyon incelemesi, model eğitimi ve **Confusion Matrix** ile performans değerlendirmesi yer almaktadır.

---

## 📂 Proje İçeriği

* 📊 **Exploratory Data Analysis (EDA)**
* 🔗 **Correlation Analysis (Heatmap & Target Correlation)**
* 🤖 **Machine Learning Modeli (Classification)**
* 📈 **Confusion Matrix & Classification Report**
* 🧪 Model değerlendirme ve görselleştirme

---

## 🧾 Kullanılan Özellikler

Veri setinde yer alan bazı temel değişkenler:

* `age` – Yaş
* `sex` – Cinsiyet
* `cp` – Göğüs ağrısı tipi
* `trestbps` – Dinlenme kan basıncı
* `chol` – Kolesterol
* `thalach` – Maksimum kalp atış hızı
* `oldpeak` – ST depresyonu
* `target` – Kalp hastalığı durumu (0: Yok, 1: Var)

---

## ⚙️ Kullanılan Kütüphaneler

```bash
pandas
numpy
matplotlib
seaborn
scikit-learn
```

---

## 🚀 Modelleme Süreci

1. Veri seti yüklendi ve ön işleme yapıldı
2. Korelasyon analizi ile hedef değişkene etkili özellikler incelendi
3. Veri train-test olarak bölündü
4. Classification modeli eğitildi (örn. Logistic Regression)
5. Model performansı **Confusion Matrix** ve **Classification Report** ile değerlendirildi

---

## 📊 Confusion Matrix

Modelin tahmin performansı aşağıdaki metriklerle ölçülmüştür:

* True Positive (TP)
* True Negative (TN)
* False Positive (FP)
* False Negative (FN)

Confusion Matrix, seaborn heatmap ile görselleştirilmiştir.

---

## ▶️ Çalıştırma

```bash
python main.py
```

veya Jupyter Notebook üzerinden adım adım çalıştırabilirsiniz.

---

## 📌 Sonuç

Bu proje, temel bir sağlık verisi üzerinde **makine öğrenmesi pipeline’ının** nasıl kurulacağını göstermektedir. Geliştirmeye açıktır ve farklı modeller (Random Forest, XGBoost vb.) eklenebilir.

---

## 👤 Yazar

* GitHub: [https://github.com/KULLANICI_ADI](https://github.com/KULLANICI_ADI)

---

⭐ Repo hoşuna gittiyse yıldızlamayı unutma!
