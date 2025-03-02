# EXCEL VERİ SETİ ANALİZ RAPORU

## 1. VERİ SETİ GENEL BİLGİLERİ

**Veri Seti Boyutu**: 250000 satır, 12 sütun

**Sütunlar**:
- Customer ID: int64
- Purchase Date: datetime64[ns]
- Product Category: object
- Product Price: int64
- Quantity: int64
- Total Purchase Amount: int64
- Payment Method: object
- Returns: float64
- Customer Name: object
- Age: int64
- Gender: object
- Churn: int64

**Eksik Değerler**:
- Returns: 47382.0 kayıt (%18.95)

## 2. TEMEL ANALİZLER

### Kategorik Değişken Analizleri

**Product Category** sütunu için en sık görülen değerler:
- Electronics: 62630 (%25.05)
- Clothing: 62581 (%25.03)
- Home: 62542 (%25.02)
- Books: 62247 (%24.90)

**Payment Method** sütunu için en sık görülen değerler:
- Credit Card: 83547 (%33.42)
- PayPal: 83441 (%33.38)
- Cash: 83012 (%33.20)

### Sayısal Değişken Analizleri

**Customer ID** sütunu istatistikleri:
- Minimum: 1
- Maksimum: 50000
- Ortalama: 25017.632092
- Medyan: 25011.0
- Standart Sapma: 14412.515718385497

**Product Price** sütunu istatistikleri:
- Minimum: 10
- Maksimum: 500
- Ortalama: 254.742724
- Medyan: 255.0
- Standart Sapma: 141.73810407868595

**Quantity** sütunu istatistikleri:
- Minimum: 1
- Maksimum: 5
- Ortalama: 3.004936
- Medyan: 3.0
- Standart Sapma: 1.4147365980360327

### Korelasyon Analizi

Önemli korelasyonlar (mutlak değeri 0.3'ten büyük olanlar):
- Product Price ve Total Purchase Amount: 0.720
- Total Purchase Amount ve Product Price: 0.720
- Quantity ve Total Purchase Amount: 0.609
- Total Purchase Amount ve Quantity: 0.609

## 3. SONUÇ VE ÖNERİLER

Bu analiz, veri setinin yapısı ve içeriği hakkında temel içgörüler sunmaktadır. Daha detaylı analizler için 'analiz_sonuclari_xlsx' klasöründeki grafikleri inceleyebilirsiniz.

**Önerilen İleri Analizler**:
- Bulguları doğrulamak için daha detaylı istatistiksel testler yapılması
- Verinin daha temiz hale getirilmesi ve eksik değerlerin işlenmesi
- Kategori ve sayısal değişkenler arasındaki ilişkilerin daha detaylı incelenmesi
