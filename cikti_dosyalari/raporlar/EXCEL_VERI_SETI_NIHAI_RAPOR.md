# PROJE.XLSX VERİ SETİ NİHAİ ANALİZ RAPORU

## YÖNETİCİ ÖZETİ

Bu rapor, proje.xlsx veri seti üzerinde gerçekleştirilen kapsamlı bir veri analizi çalışmasının sonuçlarını içermektedir. Analizler, veri hazırlama, keşifsel veri analizi, görselleştirme ve müşteri segmentasyonu (RFM analizi) aşamalarını kapsamaktadır.

**Temel Bulgular:**

1. E-ticaret platformu, dengeli bir kategori dağılımı ile çeşitli ürün gruplarında faaliyet göstermektedir.
2. Yüksek iade oranları (%50 civarında) ve müşteri ayrılma oranları (%40) kritik sorunlar olarak öne çıkmaktadır.
3. Müşterilerin %21.84'ünü oluşturan "Champions" segmenti, toplam gelirlerin büyük bir kısmını sağlamaktadır.
4. 26-35 yaş aralığındaki müşteriler en yüksek ortalama satın alma tutarına sahiptir.
5. Ürün kategorileri ile cinsiyet arasında belirgin ilişkiler mevcuttur.

**Acil Eylem Gerektiren Alanlar:**
- İade oranlarının düşürülmesi
- Müşteri ayrılma oranlarının azaltılması
- At Risk ve Hibernating segmentlerindeki müşterilerin yeniden kazanılması

## 1. VERİ SETİ HAKKINDA

**Veri Seti Özellikleri:**
- 250.000 satır, 12 sütun
- Müşteri kimlik bilgileri, demografik veriler, satın alma bilgileri ve işlem detayları
- Returns (İade) sütununda %18.95 oranında eksik veri

**Değişkenler:**
- Customer ID: Müşteri kimliği
- Purchase Date: Satın alma tarihi
- Product Category: Ürün kategorisi (Electronics, Clothing, Home, Books)
- Product Price: Ürün fiyatı (10 TL - 500 TL)
- Quantity: Satın alınan ürün miktarı (1-5)
- Total Purchase Amount: Toplam satın alma tutarı (10 TL - 2.500 TL)
- Payment Method: Ödeme yöntemi (Credit Card, PayPal, Cash)
- Returns: İade bilgisi (Yes/No)
- Customer Name: Müşteri adı
- Age: Müşteri yaşı (18-70)
- Gender: Müşteri cinsiyeti (Male/Female)
- Churn: Müşteri ayrılma durumu (0: Devam eden, 1: Ayrılan)

## 2. KATEGORİK DEĞİŞKEN ANALİZİ

### Ürün Kategorileri
Dört ana kategori dengeli bir dağılım göstermektedir:
- Electronics: %25.05
- Clothing: %25.03
- Home: %25.02
- Books: %24.90

### Ödeme Yöntemleri
Ödeme yöntemleri arasında da dengeli bir dağılım gözlenmiştir:
- Kredi Kartı: %33.42
- PayPal: %33.38
- Nakit: %33.20

### Cinsiyet Dağılımı
Müşterilerin cinsiyet dağılımı:
- Erkek: %50.27
- Kadın: %49.73

### İade Durumu
İade bilgisi bulunan kayıtlar incelendiğinde:
- İade Edilen: %50.08
- İade Edilmeyen: %49.92

### Müşteri Ayrılma (Churn) Durumu
Müşterilerin ayrılma durumu:
- Devam Eden Müşteriler: %60 (tahmini)
- Ayrılan Müşteriler: %40 (tahmini)

## 3. SAYISAL DEĞİŞKEN ANALİZİ

### Ürün Fiyatları
- Minimum: 10 TL
- Maksimum: 500 TL
- Ortalama: 254.74 TL
- Medyan: 255 TL
- Standart Sapma: 141.74 TL

### Sipariş Miktarları
- Minimum: 1 ürün
- Maksimum: 5 ürün
- Ortalama: 3.00 ürün
- Medyan: 3 ürün
- Standart Sapma: 1.41 ürün

### Toplam Satın Alma Tutarları
- Minimum: 10 TL
- Maksimum: 2.500 TL
- Ortalama: 765.95 TL
- Medyan: 604 TL
- Standart Sapma: 593.49 TL

### Yaş Dağılımı
- Yaş Aralığı: 18-70
- En aktif yaş grubu: 26-35

## 4. RFM ANALİZİ VE MÜŞTERİ SEGMENTASYONU

RFM analizi, müşterileri Recency (Son satın alma tarihi), Frequency (Satın alma sıklığı) ve Monetary (Harcama tutarı) parametrelerine göre segmentlere ayıran bir yöntemdir.

### Segment Dağılımı

| Segment                     | Müşteri Sayısı | Yüzde (%) |
|-----------------------------|----------------|-----------|
| Champions                   | 10.846         | 21.84     |
| Potential Loyalists         | 8.383          | 16.88     |
| Lost                        | 6.390          | 12.87     |
| At Risk                     | 5.335          | 10.74     |
| Customers Needing Attention | 4.425          | 8.91      |
| Loyal Customers             | 3.923          | 7.90      |
| About to Sleep              | 2.817          | 5.67      |
| New Customers               | 2.744          | 5.53      |
| Promising                   | 2.137          | 4.30      |
| Hibernating                 | 1.742          | 3.51      |
| Cant Lose Them              | 919            | 1.85      |

### Önemli Segment Özellikleri

**Champions (En Değerli Müşteriler):**
- Son alışveriş: Ortalama 79 gün önce
- Alışveriş sıklığı: Ortalama 7.6 kez
- Toplam harcama: Ortalama 6.118 TL
- Pazarlama stratejisi: Sadakat programları, özel indirimler ve VIP hizmetler

**At Risk (Risk Altındaki Müşteriler):**
- Son alışveriş: Ortalama 534 gün önce
- Alışveriş sıklığı: Ortalama 5.3 kez
- Toplam harcama: Ortalama 4.350 TL
- Pazarlama stratejisi: Acil win-back kampanyaları

**New Customers (Yeni Müşteriler):**
- Son alışveriş: Ortalama 38 gün önce
- Alışveriş sıklığı: Ortalama 4.3 kez
- Toplam harcama: Ortalama 1.963 TL
- Pazarlama stratejisi: Satın alma deneyimini iyileştirmeye odaklanma

## 5. DİĞER ÖNEMLİ ANALİZLER

### Korelasyon Analizi
- Ürün Fiyatı ve Toplam Satın Alma Tutarı arasında güçlü pozitif korelasyon (0.72)
- Ürün Miktarı ve Toplam Satın Alma Tutarı arasında pozitif korelasyon (0.61)
- Yaş ve Satın Alma Tutarı arasında zayıf pozitif korelasyon

### Cinsiyet ve Kategori İlişkisi
- Erkek müşteriler daha çok Electronics kategorisinde alışveriş yapmaktadır
- Kadın müşteriler Clothing kategorisinde daha aktiftir
- Home ve Books kategorilerinde cinsiyet dağılımı daha dengelidir

### Yaş Grubu ve Satın Alma İlişkisi
- 26-35 yaş aralığı en yüksek ortalama satın alma tutarına sahiptir
- 18-25 ve 56+ yaş grupları en düşük ortalama satın alma tutarına sahiptir

### Segment Bazlı İade Oranları
- At Risk müşterilerde en yüksek iade oranı bulunmaktadır
- New Customers segmentinde iade oranları ortalamanın altındadır

## 6. ÖNERİLER

### İşletme Stratejisi İçin Öneriler

**1. İade Oranlarını Azaltma Stratejileri:**
- Ürün açıklamalarının ve görsellerinin iyileştirilmesi
- Ürün kalitesinin artırılması
- Müşteri beklentilerinin daha iyi yönetilmesi
- Özellikle Electronics kategorisinde ürün bilgilendirmelerinin geliştirilmesi

**2. Müşteri Sadakatini Artırma Stratejileri:**
- Champions ve Loyal Customers segmentleri için özel sadakat programları geliştirilmesi
- Kişiselleştirilmiş pazarlama stratejileri uygulanması
- Düzenli alışveriş yapan müşterilere özel indirimler sunulması
- Müşteri deneyimini iyileştirmek için geribildirim mekanizmaları oluşturulması

**3. Kritik Segmentlere Özel Stratejiler:**
- At Risk ve Hibernating müşteriler için acil win-back kampanyaları düzenlenmesi
- New Customers ve Potential Loyalists müşterilerinin sadık müşterilere dönüştürülmesi
- About to Sleep segmentindeki müşterilerin aktifleştirilmesi için özel teklifler

**4. Kategori Bazlı Stratejiler:**
- Electronics kategorisinde iade oranını düşürmek için detaylı ürün bilgilendirmesi
- Clothing kategorisinde cinsiyet bazlı özel kampanyalar
- Books kategorisindeki düşük iade oranlarının nedenlerinin diğer kategorilere uygulanması

**5. Yaş Gruplarına Özel Stratejiler:**
- 26-35 yaş grubu için özel VIP programlar
- 18-25 yaş grubuna özel giriş kampanyaları ve fiyat stratejileri
- 56+ yaş grubu için kullanıcı dostu alışveriş deneyimi

### İleri Analiz Adımları

**1. Daha Detaylı Segmentasyon:**
- RFM analizi ile elde edilen segmentlerin davranışsal faktörlerle birleştirilmesi
- Müşteri yaşam döngüsü analizi

**2. Sepet Analizi:**
- Birlikte satın alınan ürünlerin tespiti
- Çapraz satış fırsatlarının değerlendirilmesi

**3. Tahmini Modeller:**
- Müşteri ayrılma (churn) tahmin modelleri
- Ürün tavsiye sistemleri
- Gelecek dönem satış tahminleri

**4. Mevsimsellik Analizi:**
- Satış trendlerinin ve mevsimselliğin detaylı analizi
- Sezonluk kampanya planlaması

## 7. SONUÇ

Bu kapsamlı analiz çalışması, işletmenin mevcut durumu, müşteri segmentleri ve ürün performansı hakkında önemli içgörüler sunmaktadır. Özellikle yüksek iade oranları ve müşteri ayrılma oranları, acil müdahale gerektiren alanlar olarak öne çıkmaktadır.

Müşteri segmentasyonu sonuçları, değerli müşterilerin korunması ve potansiyel müşterilerin geliştirilmesi için hedefe yönelik stratejiler geliştirme imkanı sunmaktadır. Her segment için özelleştirilmiş pazarlama stratejileri, müşteri sadakatini artırmak ve genel işletme performansını iyileştirmek için kritik öneme sahiptir.

Bu rapordaki bulgular ve öneriler, veri odaklı karar alma süreçlerine katkı sağlayarak işletmenin rekabet avantajını artırmasına yardımcı olacaktır. Analizlerin düzenli olarak tekrarlanması ve stratejilerin sonuçlarının değerlendirilmesi, sürekli iyileştirme için önemlidir. 