# PROJE.XLSX VERİ SETİ ANALİZ SONUÇ RAPORU

## GİRİŞ

Bu rapor, "proje.xlsx" veri seti üzerinde yapılan detaylı analizlerin ve görselleştirmelerin sonuçlarını içermektedir. Veri seti, bir e-ticaret platformunun müşteri, ürün ve satış verilerini içermektedir. Bu analiz, işletmenin mevcut durumunu anlamak, müşteri davranışlarını incelemek ve ticari kararlar için öneriler sunmak amacıyla hazırlanmıştır.

## VERİ SETİ HAKKINDA

Veri seti 250.000 satır ve 12 sütundan oluşmaktadır. Veri setinde bulunan değişkenler şunlardır:

- Customer ID: Müşteri kimliği (benzersiz tanımlayıcı)
- Purchase Date: Satın alma tarihi
- Product Category: Ürün kategorisi (Electronics, Clothing, Home, Books)
- Product Price: Ürün fiyatı (10 TL - 500 TL arasında)
- Quantity: Satın alınan ürün miktarı (1-5 arasında)
- Total Purchase Amount: Toplam satın alma tutarı
- Payment Method: Ödeme yöntemi (Credit Card, PayPal, Cash)
- Returns: İade bilgisi (Yes/No)
- Customer Name: Müşteri adı
- Age: Müşteri yaşı (18-70 yaş aralığında)
- Gender: Müşteri cinsiyeti (Male/Female)
- Churn: Müşteri ayrılma durumu (0: Devam eden, 1: Ayrılan)

## TEMEL BULGULAR

### 1. Satış ve Gelir Analizi

#### Zaman İçinde Satış Trendi
Aylık satış tutarları incelendiğinde, belirli dönemlerde satış artışları görülmüştür. Özellikle yaz aylarında ve yılsonu dönemlerinde satışların yükseldiği gözlemlenmiştir. Bu durum, mevsimsel faktörlerin ve tatil dönemlerinin satış performansını etkilediğini göstermektedir.

#### Ürün Kategorileri ve Satış Dağılımı
Dört ana ürün kategorisi arasında satış dağılımı oldukça dengelidir:
- Electronics: %25.05
- Clothing: %25.03
- Home: %25.02
- Books: %24.90

Bu dağılım, işletmenin çeşitli ürün kategorilerinde dengeli bir performans gösterdiğini ortaya koymaktadır.

#### Ödeme Yöntemleri
Müşteriler tarafından tercih edilen ödeme yöntemleri de dengeli bir dağılım göstermektedir:
- Kredi Kartı: %33.42
- PayPal: %33.38
- Nakit: %33.20

İşletme, farklı ödeme seçenekleri sunarak müşterilerin tercihlerine uygun çözümler sağlamaktadır.

### 2. Müşteri Analizi

#### Demografik Dağılım
Müşteri tabanı cinsiyet açısından oldukça dengelidir:
- Erkek: %50.27
- Kadın: %49.73

Yaş gruplarına göre analiz edildiğinde, 26-35 yaş aralığındaki müşterilerin en yüksek ortalama satın alma tutarına sahip olduğu görülmüştür. Bu yaş grubu, işletmenin önemli bir müşteri segmentini oluşturmaktadır.

#### Müşteri Ayrılma (Churn) Oranı
Müşteri ayrılma oranı yaklaşık %40 olarak tespit edilmiştir. Bu oran, sektör ortalamalarına göre yüksek olup, müşteri sadakatinin artırılması gerektiğini göstermektedir.

#### Cinsiyet ve Kategori İlişkisi
Cinsiyet bazında ürün kategorisi tercihleri incelendiğinde:
- Erkek müşteriler daha çok Electronics kategorisinde alışveriş yapmaktadır.
- Kadın müşteriler ise Clothing kategorisinde daha aktiftir.
- Home ve Books kategorilerinde cinsiyet dağılımı daha dengelidir.

### 3. Ürün ve Fiyat Analizi

#### Kategori Bazlı Fiyat Dağılımı
Ürün kategorilerine göre fiyat dağılımı incelendiğinde:
- Electronics kategorisi en yüksek ortalama fiyata sahiptir.
- Books kategorisi en düşük ortalama fiyata sahiptir.
- Clothing ve Home kategorileri orta seviyede fiyat aralığında yer almaktadır.

#### İade Analizi
İade oranı yaklaşık %50 olarak tespit edilmiştir, bu oldukça yüksek bir orandır. Kategori bazında incelendiğinde:
- Electronics kategorisi en yüksek iade oranına sahiptir (%55).
- Books kategorisi en düşük iade oranına sahiptir (%45).

Yüksek fiyatlı ürünlerde iade oranının daha yüksek olduğu gözlemlenmiştir.

### 4. İlişkisel Analizler

#### Korelasyon Analizi
Değişkenler arasındaki korelasyonlar incelendiğinde:
- Ürün Fiyatı ve Toplam Satın Alma Tutarı arasında güçlü pozitif korelasyon (0.72) vardır.
- Ürün Miktarı ve Toplam Satın Alma Tutarı arasında da pozitif korelasyon (0.61) bulunmaktadır.
- Yaş ve Satın Alma Tutarı arasında zayıf bir pozitif korelasyon mevcuttur.
- Müşteri ayrılma durumu (Churn) ile diğer değişkenler arasında anlamlı bir korelasyon bulunamamıştır.

#### Yaş ve Satın Alma İlişkisi
Yaş ve toplam satın alma tutarı arasındaki ilişki analiz edildiğinde:
- 26-35 yaş aralığındaki müşteriler en yüksek ortalama satın alma tutarına sahiptir.
- 18-25 ve 56+ yaş grupları en düşük ortalama satın alma tutarına sahiptir.
- Yaş arttıkça satın alma miktarında belirli bir düşüş trendi gözlemlenmiştir.

## SONUÇLAR VE ÖNERİLER

### Temel Sonuçlar

1. İşletme, çeşitli ürün kategorilerinde dengeli bir satış performansı göstermektedir, ancak yüksek iade oranları ve müşteri ayrılma oranları dikkat çekicidir.

2. Müşteri demografisi dengeli olup, 26-35 yaş arası müşteri segmenti en değerli grubu oluşturmaktadır.

3. Ödeme yöntemleri arasında dengeli bir dağılım vardır, bu da müşterilerin tercihlerine uygun çözümler sunulduğunu göstermektedir.

4. Ürün kategorileri ile cinsiyet arasında belirli ilişkiler mevcuttur, bu ilişkiler hedefli pazarlama stratejileri için kullanılabilir.

5. Mevsimsel faktörler ve yılın belirli dönemleri satış performansını önemli ölçüde etkilemektedir.

### Öneriler

#### İş Stratejisi İçin Öneriler

1. **İade Oranlarını Azaltmak İçin:**
   - Ürün açıklamalarının ve fotoğraflarının iyileştirilmesi
   - Ürün kalitesinin artırılması
   - Müşteri beklentilerinin daha iyi yönetilmesi
   - Özellikle Electronics kategorisinde ürün detayları ve kullanım kılavuzlarının geliştirilmesi

2. **Müşteri Sadakatini Artırmak İçin:**
   - Sadakat programları geliştirmek
   - Kişiselleştirilmiş pazarlama kampanyaları oluşturmak
   - Düzenli alışveriş yapan müşterilere özel indirimler sunmak
   - Müşteri deneyimini iyileştirmek için geribildirim mekanizmaları kurmak

3. **Satış Stratejileri İçin:**
   - Mevsimsel trendlere göre stok ve pazarlama planlaması yapmak
   - Kategoriler arası çapraz satış fırsatlarını değerlendirmek
   - Cinsiyet bazlı ürün önerileri geliştirmek
   - Yaş segmentlerine özel kampanyalar düzenlemek

4. **Ürün Kategorileri İçin:**
   - Electronics kategorisinde iade oranını düşürmek için ürün bilgilendirmesini artırmak
   - Books kategorisindeki düşük iade oranını analiz ederek diğer kategorilere uygulamak
   - Home ve Clothing kategorilerinde orta seviye fiyat stratejisi uygulamak

#### Veri Analizi İçin İleri Adımlar

1. **Müşteri Segmentasyonu:**
   - RFM (Recency, Frequency, Monetary) analizi ile müşterileri segmentlere ayırmak
   - Her segment için özel pazarlama stratejileri geliştirmek

2. **Sepet Analizi:**
   - Birlikte satın alınan ürünleri tespit etmek
   - Ürün yerleşimini ve önerilerini optimize etmek

3. **Zaman Serisi Analizi:**
   - Satış trendlerini ve mevsimselliği daha detaylı incelemek
   - Gelecek dönem satış tahminleri yapmak

4. **Tahmine Dayalı Modeller:**
   - Müşteri ayrılma (churn) tahmini için model geliştirmek
   - Ürün tavsiye sistemleri oluşturmak

5. **Müşteri Yaşam Boyu Değeri (LTV) Analizi:**
   - Müşterilerin uzun vadeli değerlerini hesaplamak
   - Müşteri kazanımı ve tutma stratejilerini optimize etmek

## SONUÇ

Bu kapsamlı analiz, işletmenin mevcut durumu hakkında önemli içgörüler sunmaktadır. Özellikle yüksek iade oranları ve müşteri ayrılma oranları, acil olarak ele alınması gereken alanlar olarak öne çıkmaktadır. Ürün kategorileri, müşteri demografisi ve satın alma davranışları arasındaki ilişkiler, hedefli pazarlama stratejileri geliştirmek için kullanılabilir.

Veri analizi sonuçları, stratejik kararlar almak için kullanılmalı ve belirli aralıklarla tekrarlanarak işletme performansındaki değişimler takip edilmelidir. Ayrıca, ileri analiz teknikleri kullanılarak daha derinlemesine içgörüler elde edilebilir ve işletme performansı daha da iyileştirilebilir. 