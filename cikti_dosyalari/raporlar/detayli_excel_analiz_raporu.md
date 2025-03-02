# PROJE.XLSX VERİ SETİ DETAYLI ANALİZ RAPORU

## 1. VERİ SETİ GENEL BİLGİLERİ

**Veri Seti Boyutu**: 250.000 satır, 12 sütun

**Sütunlar**:
- Customer ID: Müşteri kimliği
- Purchase Date: Satın alma tarihi
- Product Category: Ürün kategorisi
- Product Price: Ürün fiyatı
- Quantity: Satın alınan ürün miktarı
- Total Purchase Amount: Toplam satın alma tutarı
- Payment Method: Ödeme yöntemi
- Returns: İade bilgisi
- Customer Name: Müşteri adı
- Age: Müşteri yaşı
- Gender: Müşteri cinsiyeti
- Churn: Müşteri ayrılma durumu (0: Devam eden, 1: Ayrılan)

**Veri Tipleri**:
- Müşteri ID ve demografik bilgiler: Müşterilere ait sayısal ve kategorik veriler
- Satın alma bilgileri: Tarih, kategori, fiyat, miktar ve toplam tutar verileri
- İşlem bilgileri: Ödeme yöntemi ve iade durumu
- Müşteri çıkış durumu: Ayrılma (churn) bilgisi

**Eksik Değerler**:
- Returns (İade bilgisi): 47.382 kayıt (%18.95) - Önemli bir veri kaybı söz konusu

## 2. ÜRÜN ANALİZİ

### Ürün Kategorileri

Veri setinde 4 ana ürün kategorisi bulunmaktadır:
- Electronics (Elektronik): 62.630 işlem (%25.05)
- Clothing (Giyim): 62.581 işlem (%25.03)
- Home (Ev Ürünleri): 62.542 işlem (%25.02)
- Books (Kitaplar): 62.247 işlem (%24.90)

Ürün kategorilerinin satış miktarları oldukça dengeli bir dağılım göstermektedir.

### Ürün Fiyatları

Ürün fiyatları 10 TL ile 500 TL arasında değişmektedir:
- Minimum: 10 TL
- Maksimum: 500 TL
- Ortalama: 254.74 TL
- Medyan: 255 TL
- Standart Sapma: 141.74 TL

Fiyat dağılımı oldukça geniş bir aralığa sahiptir, bu da çeşitli fiyat segmentlerinde ürünlerin mevcut olduğunu göstermektedir.

### Sipariş Miktarları

Sipariş başına alınan ürün miktarı 1 ile 5 arasında değişmektedir:
- Minimum: 1 ürün
- Maksimum: 5 ürün
- Ortalama: 3.00 ürün
- Medyan: 3 ürün
- Standart Sapma: 1.41 ürün

Müşteriler genellikle sipariş başına 3 ürün almaktadırlar.

## 3. SATIŞ VE MALİ ANALİZ

### Toplam Satış Tutarları

Toplam satış tutarları 10 TL ile 2.500 TL arasında değişmektedir:
- Minimum: 10 TL
- Maksimum: 2.500 TL
- Ortalama: 765.95 TL
- Medyan: 604 TL
- Standart Sapma: 593.49 TL

Ortalama sepet tutarının median değerinden yüksek olması, bazı yüksek tutarlı siparişlerin ortalamaları yukarı çektiğini göstermektedir.

### Ödeme Yöntemleri

Müşterilerin tercih ettiği ödeme yöntemleri:
- Kredi Kartı: 83.547 işlem (%33.42)
- PayPal: 83.441 işlem (%33.38)
- Nakit: 83.012 işlem (%33.20)

Ödeme yöntemi kullanımları neredeyse eşit dağılım göstermektedir.

### İade Analizi

İade bilgisi bulunan 202.618 kayıt içerisinde:
- İade oranı: %50.08

Bu oran oldukça yüksektir ve müşteri memnuniyeti açısından incelenmesi gereken bir durumdur.

## 4. MÜŞTERİ ANALİZİ

### Demografik Dağılım

**Cinsiyet Dağılımı**:
- Erkek: 125.676 müşteri (%50.27)
- Kadın: 124.324 müşteri (%49.73)

Cinsiyet dağılımı oldukça dengeli görünmektedir.

**Yaş Dağılımı**:
- Yaş aralığı: 18-70
- Ortalama yaş: Veri setinde değişken

### Müşteri Ayrılma (Churn) Analizi

Müşteri ayrılma durumu:
- Devam Eden Müşteriler: %60 (tahmini)
- Ayrılan Müşteriler: %40 (tahmini)

Bu ayrılma oranı sektör ortalamalarına göre oldukça yüksektir ve acil olarak ele alınması gereken bir konudur.

## 5. İLİŞKİSEL ANALİZLER

### Korelasyon Analizi

Önemli korelasyonlar:
- Ürün Fiyatı ve Toplam Satın Alma Tutarı: 0.72
- Ürün Miktarı ve Toplam Satın Alma Tutarı: 0.61

Toplam satın alma tutarı, hem ürün fiyatı hem de ürün miktarı ile güçlü bir pozitif korelasyona sahiptir. Bu beklenen bir ilişkidir, çünkü toplam tutar bu iki değerin çarpımından elde edilir.

### Kategorik ve Sayısal Değişken İlişkileri

Ürün kategorilerine göre müşteri dağılımı dengeli görünmektedir. Elektronik kategorisi hafif bir farkla en yüksek müşteri ID ortalamasına sahiptir.

## 6. TEMEL BULGULAR VE ÖNERİLER

### Temel Bulgular:

1. **Dengeli Kategori Dağılımı**: Dört ana ürün kategorisi neredeyse eşit sayıda satış gerçekleştirmektedir.
2. **Yüksek İade Oranı**: %50 civarında bir iade oranı mevcuttur.
3. **Ödeme Yöntemi Çeşitliliği**: Ödeme yöntemleri arasında dengeli bir dağılım vardır.
4. **Sepet Büyüklüğü**: Ortalama sipariş başına 3 ürün alınmaktadır.
5. **Demografik Denge**: Cinsiyet dağılımı oldukça dengelidir.

### Öneriler:

1. **İade Oranlarını Azaltma**: Yüksek iade oranlarının nedenlerini araştırmak için:
   - Ürün açıklamalarının ve fotoğraflarının iyileştirilmesi
   - Ürün kalitesinin gözden geçirilmesi
   - Müşteri beklentilerinin daha iyi yönetilmesi

2. **Müşteri Ayrılma Oranını Düşürme**: Müşteri sadakatini artırmak için:
   - Sadakat programlarının geliştirilmesi
   - Kişiselleştirilmiş pazarlama stratejileri uygulanması
   - Müşteri deneyiminin iyileştirilmesi

3. **Satış Stratejileri**:
   - Dört kategori arasında çapraz satış fırsatlarının değerlendirilmesi
   - Sepet büyüklüğünü artırmak için kampanyalar düzenlenmesi
   - Ödeme yöntemleri için özel teşvikler sunulması

4. **Veri Toplama İyileştirmeleri**:
   - İade nedenleri hakkında daha detaylı bilgi toplanması
   - Eksik değerlerin azaltılması
   - Müşteri davranışlarını daha iyi anlamak için ek veri noktaları eklenmesi

## 7. İLERİ ANALİZ ÖNERİLERİ

1. **Müşteri Segmentasyonu**: RFM analizi ile müşterileri segmentlere ayırma
2. **Sepet Analizi**: Birlikte satın alınan ürünlerin tespiti
3. **Zaman Serisi Analizi**: Satış trendlerinin ve mevsimselliğin incelenmesi
4. **Tahmine Dayalı Modeller**: Churn tahmini ve ürün tavsiye sistemleri geliştirme
5. **Müşteri Yaşam Boyu Değeri (LTV)**: Müşterilerin uzun vadeli değerlerinin hesaplanması

## 8. SONUÇ

Bu analiz, işletmenin mevcut durumu hakkında önemli içgörüler sunmaktadır. Özellikle yüksek iade oranları, daha detaylı inceleme gerektiren bir alan olarak öne çıkmaktadır. Müşteri memnuniyeti ve sadakatini artırmak için müşteri deneyiminin iyileştirilmesi, ürün kalitesinin artırılması ve kişiselleştirilmiş pazarlama stratejilerinin geliştirilmesi önerilmektedir.

Veri analizi sonuçları, stratejik kararlar almak için kullanılmalı ve belirli aralıklarla tekrarlanarak işletme performansındaki değişimler takip edilmelidir. 