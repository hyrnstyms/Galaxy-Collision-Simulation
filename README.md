# 🌌 N-Body Galaxy Collision Simulation

Bu proje, **N-body problemi** kapsamında iki galaksinin kütleçekim etkileşimini ve çarpışma sürecini sayısal yöntemler kullanarak simüle etmektedir. Simülasyon, parçacıkların (yıldızların) zamana bağlı hareketini hesaplayarak galaksi dinamiklerini görselleştirir.

---

## 📌 Proje Tanımı

Bu proje, **iki galaksinin çarpışmasını** temsil eden çok parçacıklı bir **N-body simülasyonu**dur. Her galaksi, çok sayıda yıldızın (parçacığın) kütleçekim kuvvetleri altında hareket etmesiyle modellenmiştir. Simülasyon boyunca her bir parçacığın konumu ve hızı, Newton mekaniğine dayalı denklemler kullanılarak zaman adımlarında güncellenir.

Amaç, galaksi çarpışmaları sırasında ortaya çıkan **yapısal bozulmalar, yörünge değişimleri ve dinamik etkileşimleri** gözlemleyebilmektir. Bu tür simülasyonlar, astrofizik ve hesaplamalı fizik alanlarında yaygın olarak kullanılmaktadır.

---

##  Proje İçeriği

* Kütleçekimsel N-body sistemi modellemesi
* İki galaksi için başlangıç konum ve hız dağılımlarının oluşturulması
* Sayısal integrasyon yöntemleri ile zamanla evrim
* Parçacık hareketlerinin 2B düzlemde görselleştirilmesi
* Animasyon ile çarpışma sürecinin izlenmesi

---

##  Kullanılan Yöntemler

* **Newton’un Evrensel Çekim Yasası**
* Sayısal integrasyon teknikleri
* Parçacık tabanlı simülasyon
* Zaman karmaşıklığı: **O(N²)** (tüm parçacık etkileşimleri)

---

##  Kullanılan Teknolojiler

* Python 3
* NumPy
* Matplotlib
* Jupyter Notebook
* (Opsiyonel) ipywidgets – etkileşimli kontroller için

---

## 📂 Dosya Yapısı

```
nbody-galaxy-collision-simulation/
│
├─ NbodySimulation.ipynb   # Ana simülasyon notebook'u (çıktılar temizlenmiştir)
├─ README.md               # Proje dokümantasyonu
└─ requirements.txt        # Gerekli Python paketleri
```

---

##  Çalıştırma Talimatları

### 1️⃣ Gerekli paketleri yükleyin

```bash
pip install -r requirements.txt
```

veya notebook içinde:

```python
!pip install numpy matplotlib ipywidgets
```

---

### 2️⃣ Notebook'u çalıştırın

```bash
jupyter notebook NbodySimulation.ipynb
```

veya VS Code / Colab üzerinden tüm hücreleri sırayla çalıştırın.

---

## ☁️ Google Colab Üzerinden Çalıştırma

Notebook, Google Colab üzerinde doğrudan çalıştırılabilir:

🔗 **Colab Linki:**
[https://colab.research.google.com/drive/1GefIMJmg9M_FootUhDMHVF24_zTl1gN0?usp=sharing#scrollTo=yO6qSawvhRhq]

> ⚠️ Not: Colab ortamında animasyonların doğru görüntülenmesi için tüm hücreleri sırasıyla çalıştırınız.

---

##  GitHub Notu

Bu repodaki Jupyter Notebook dosyasında **çıktılar (outputs) bilinçli olarak temizlenmiştir**. Bunun sebebi dosya boyutunu küçültmek ve GitHub önizleme sınırlarını aşmamaktır.

Simülasyonu ve animasyonları görmek için:

```
Runtime / Kernel → Restart & Run All
```

---

##  Proje Amacı

Bu projenin temel amacı, **N-body problemini** temel alarak galaksi çarpışmaları gibi karmaşık fiziksel sistemlerin **sayısal yöntemler** yardımıyla nasıl modellenebileceğini göstermektir. Özellikle analitik çözümü mümkün olmayan çok parçacıklı sistemlerde, nümerik integrasyon tekniklerinin önemi vurgulanmaktadır.

Bu kapsamda proje ile:

* Çok sayıda parçacıktan oluşan bir sistemde **kütleçekim etkileşimlerinin** nasıl hesaplandığı,
* Başlangıç koşullarının (konum, hız, kütle) sistemin zamanla evrimine etkisi,
* Farklı sayısal integrasyon yöntemlerinin sistem kararlılığı ve doğruluğu üzerindeki rolü,
* Galaksi çarpışmaları sırasında ortaya çıkan **dinamik yapı değişimlerinin** görselleştirilmesi

amaçlanmaktadır.

Bu çalışma; sayısal analiz, hesaplamalı fizik ve astrofizik alanlarında kullanılan yöntemlerin **eğitim ve akademik amaçlı** bir uygulamasıdır.

---


