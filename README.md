# E-Ticaret Veri Analizi Projesi

## Proje Hakkında

Bu proje, bir e-ticaret platformunun müşteri, ürün ve satış verilerini analiz ederek, işletme performansını değerlendirmeyi ve stratejik kararlar için öneriler sunmayı amaçlamaktadır. Veri analizi çalışmaları, Python programlama dili ve çeşitli veri analizi kütüphaneleri kullanılarak gerçekleştirilmiştir.

## Veri Seti

Proje kapsamında "proje.xlsx" adlı Excel formatındaki veri seti kullanılmıştır. Veri seti, 250.000 satır ve 12 sütundan oluşmaktadır ve aşağıdaki bilgileri içermektedir:

- Müşteri kimlik ve demografik bilgileri (Yaş, Cinsiyet)
- Satın alma tarihleri ve tutarları
- Ürün kategorileri ve fiyatları
- Ödeme yöntemleri
- İade bilgileri
- Müşteri ayrılma (churn) durumu

## Proje Yapısı

Projede bulunan dosyalar ve klasörler:

- **proje_analiz_xlsx.py**: Temel veri analizi işlemlerini gerçekleştiren Python betiği
- **detayli_gorselleştirme.py**: Detaylı görselleştirmeler oluşturan Python betiği
- **rfm_analizi.py**: Müşteri segmentasyonu için RFM analizi yapan Python betiği
- **analiz_sonuclari_xlsx/**: Temel analiz sonuçlarını ve görsellerini içeren klasör
- **detayli_gorseller/**: Detaylı görselleştirmelerin kaydedildiği klasör
- **rfm_analiz_sonuclari/**: RFM analizi sonuçlarını ve görsellerini içeren klasör
- **xlsx_analiz_raporu.md**: Temel analizleri içeren rapor
- **detayli_excel_analiz_raporu.md**: Detaylı analiz raporu
- **sonuc_raporu.md**: Görselleştirme analizlerinin sonuçlarını içeren rapor
- **EXCEL_VERI_SETI_NIHAI_RAPOR.md**: Tüm analizleri birleştiren kapsamlı nihai rapor

## Gerçekleştirilen Analizler

Proje kapsamında yapılan analizler:

1. **Keşifsel Veri Analizi (EDA)**:
   - Veri yapısının incelenmesi
   - Eksik değerlerin tespiti
   - Temel istatistiksel ölçümlerin hesaplanması
   - Kategorik ve sayısal değişkenlerin analizi

2. **Görselleştirme Analizleri**:
   - Çeşitli ürün kategorisi ve demografik dağılımların görselleştirilmesi
   - Zaman bazlı satış trendlerinin incelenmesi
   - İade oranlarının analizi
   - Yaş grupları ve satın alma ilişkisinin görselleştirilmesi
   - Korelasyon matrisi ve ısı haritaları

3. **RFM Analizi ve Müşteri Segmentasyonu**:
   - Recency, Frequency ve Monetary değerlerinin hesaplanması
   - Müşterilerin 11 farklı segmente ayrılması
   - Segmentlerin özelliklerinin analizi
   - Segment bazlı pazarlama stratejilerinin önerilmesi

## Temel Bulgular

Analizler sonucunda elde edilen önemli bulgular:

- Ürün kategorileri arasında dengeli bir dağılım mevcuttur
- Yüksek iade oranları (%50) ve müşteri ayrılma oranları (%40) dikkat çekicidir
- Müşterilerin %21.84'ünü oluşturan "Champions" segmenti toplam gelirin büyük bir kısmını sağlamaktadır
- 26-35 yaş aralığındaki müşteriler en yüksek ortalama satın alma tutarına sahiptir
- Ürün kategorileri ile cinsiyet arasında belirgin ilişkiler vardır

## Öneriler

Analiz sonuçlarına dayanarak sunulan öneriler:

1. **İade Oranlarını Azaltma Stratejileri**
2. **Müşteri Sadakatini Artırma Programları**
3. **Risk Altındaki Müşterileri Geri Kazanma Kampanyaları**
4. **Kategori ve Yaş Grubu Bazlı Özel Stratejiler**
5. **İleri Analiz Teknikleri ile Derinlemesine İnceleme**

## Gereksinimler

Bu projeyi çalıştırmak için aşağıdaki Python kütüphanelerine ihtiyaç vardır:

- pandas
- numpy
- matplotlib
- seaborn
- tabulate

## Kurulum

Gerekli kütüphaneleri yüklemek için:

```bash
pip install pandas numpy matplotlib seaborn tabulate
```

## Kullanım

Temel analiz betiği:
```bash
python proje_analiz_xlsx.py
```

Detaylı görselleştirme betiği:
```bash
python detayli_gorselleştirme.py
```

RFM analizi betiği:
```bash
python rfm_analizi.py
```

## Sonuç

Bu kapsamlı analiz çalışması, işletmenin mevcut durumu, müşteri segmentleri ve ürün performansı hakkında önemli içgörüler sunmaktadır. Bu rapordaki bulgular ve öneriler, veri odaklı karar alma süreçlerine katkı sağlayarak işletmenin rekabet avantajını artırmasına yardımcı olacaktır. 