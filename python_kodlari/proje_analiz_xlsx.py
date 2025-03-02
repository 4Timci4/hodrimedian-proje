import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import os

# Grafiklerdeki Türkçe karakterlerin düzgün görünmesi için
plt.rcParams['font.family'] = 'DejaVu Sans'

# Excel dosyasını okuma
print("Excel dosyası okunuyor...")
df = pd.read_excel('proje.xlsx')

# Veri setinin genel bilgilerini görüntüleme
print("\n===== VERİ SETİ GENEL BİLGİLERİ =====")
print(f"Veri seti boyutu: {df.shape[0]} satır, {df.shape[1]} sütun")
print("\nİlk 5 satır:")
print(df.head())

print("\nVeri seti bilgileri:")
print(df.info())

print("\nBetimsel istatistikler:")
print(df.describe(include='all').T)

print("\nEksik değerler:")
missing_values = df.isnull().sum()
missing_percent = (df.isnull().sum() / len(df)) * 100
missing_df = pd.DataFrame({'Eksik Değer Sayısı': missing_values, 
                           'Yüzde (%)': missing_percent})
print(missing_df[missing_df['Eksik Değer Sayısı'] > 0])

# Veri temizliği
print("\n===== VERİ TEMİZLİĞİ =====")

# Sütun isimlerini temizleme - önceden bilinmiyor, bu yüzden genel bir yaklaşım
df.columns = df.columns.str.strip()

# Veri tipi dönüşümleri - bu kısım veri yapısına göre güncellenecek
print("Veri tipleri kontrol ediliyor ve düzenleniyor...")
numeric_columns = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
object_columns = df.select_dtypes(include=['object']).columns.tolist()
date_columns = []

# Tarih sütunlarını tespit etme
for col in object_columns:
    try:
        # Test et, tarih olabilecek sütunları kontrol et
        if df[col].nunique() > 0:
            sample = df[col].dropna().iloc[0]
            if isinstance(sample, str) and ('/' in sample or '-' in sample or ':' in sample):
                pd.to_datetime(df[col], errors='coerce')
                date_columns.append(col)
                print(f"{col} sütunu tarih formatına dönüştürülüyor...")
    except:
        pass

# Tarih sütunlarını dönüştürme
for col in date_columns:
    try:
        df[col] = pd.to_datetime(df[col], errors='coerce')
        df[f'{col}_Year'] = df[col].dt.year
        df[f'{col}_Month'] = df[col].dt.month
        df[f'{col}_Day'] = df[col].dt.day
        print(f"{col} sütunu tarih formatına dönüştürüldü ve yıl/ay/gün sütunları eklendi.")
    except Exception as e:
        print(f"{col} sütunu dönüştürülürken hata: {e}")

# Sayısal olabilecek nesne sütunlarını dönüştürme
for col in object_columns:
    if col not in date_columns:
        try:
            numeric_values = pd.to_numeric(df[col], errors='coerce')
            if numeric_values.notna().sum() / len(df) > 0.5:  # Yarısından fazlası sayısal ise dönüştür
                df[col] = numeric_values
                print(f"{col} sütunu sayısal değere dönüştürüldü.")
        except:
            pass

# Veri seti yapısını kontrol etme
print("\nTemizlik sonrası veri tipi bilgileri:")
print(df.dtypes)

# Veri Analizi ve Görselleştirme
print("\n===== VERİ ANALİZİ VE GÖRSELLEŞTİRME =====")

# Grafikleri kaydetmek için klasör oluştur
output_dir = 'analiz_sonuclari_xlsx'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Kategorik sütunları bul
categorical_columns = df.select_dtypes(include=['object', 'category']).columns.tolist()
# Sayısal sütunları güncelle
numeric_columns = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
# Tarih sütunları zaten belirlenmiş durumda

print(f"\nKategorik sütunlar: {categorical_columns}")
print(f"Sayısal sütunlar: {numeric_columns}")
print(f"Tarih sütunları: {date_columns}")

# 1. Kategorik değişkenlerin analizi
print("\nKategorik değişkenler analiz ediliyor...")
for col in categorical_columns[:5]:  # İlk 5 kategorik sütunu analiz et
    try:
        if df[col].nunique() < 20:  # Çok fazla benzersiz değer yoksa
            plt.figure(figsize=(12, 6))
            value_counts = df[col].value_counts().sort_values(ascending=False).head(10)
            sns.barplot(x=value_counts.index, y=value_counts.values)
            plt.title(f'{col} Değerlerinin Dağılımı')
            plt.xlabel(col)
            plt.ylabel('Frekans')
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.savefig(f'{output_dir}/{col}_dagilimi.png')
            plt.close()
            
            print(f"{col} sütunu için en sık görülen 5 değer:")
            print(value_counts.head())
    except Exception as e:
        print(f"{col} sütunu analiz edilirken hata: {e}")

# 2. Sayısal değişkenlerin analizi
print("\nSayısal değişkenler analiz ediliyor...")
for col in numeric_columns[:5]:  # İlk 5 sayısal sütunu analiz et
    try:
        plt.figure(figsize=(10, 6))
        sns.histplot(df[col].dropna(), bins=30, kde=True)
        plt.title(f'{col} Dağılımı')
        plt.xlabel(col)
        plt.ylabel('Frekans')
        plt.tight_layout()
        plt.savefig(f'{output_dir}/{col}_dagilimi.png')
        plt.close()
        
        print(f"{col} sütunu için istatistikler:")
        print(df[col].describe())
    except Exception as e:
        print(f"{col} sütunu analiz edilirken hata: {e}")

# 3. Korelasyon analizi
if len(numeric_columns) > 1:
    try:
        print("\nKorelasyon analizi yapılıyor...")
        corr_columns = numeric_columns[:10]  # İlk 10 sayısal sütun arasındaki korelasyon
        df_corr = df[corr_columns].dropna()
        
        plt.figure(figsize=(12, 10))
        corr_matrix = df_corr.corr()
        sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
        plt.title('Değişkenler Arasındaki Korelasyon')
        plt.tight_layout()
        plt.savefig(f'{output_dir}/korelasyon_matrisi.png')
        plt.close()
        
        print("Önemli korelasyonlar:")
        # Mutlak değerce 0.3'ten büyük korelasyonları göster (kendisi hariç)
        important_corr = corr_matrix.unstack().sort_values(ascending=False)
        important_corr = important_corr[(abs(important_corr) > 0.3) & (important_corr < 1.0)]
        print(important_corr)
    except Exception as e:
        print(f"Korelasyon analizinde hata: {e}")

# 4. Kategorik ve sayısal değişken ilişkileri
if len(categorical_columns) > 0 and len(numeric_columns) > 0:
    try:
        print("\nKategorik ve sayısal değişken ilişkileri analiz ediliyor...")
        cat_col = categorical_columns[0]  # İlk kategorik sütun
        num_col = numeric_columns[0]  # İlk sayısal sütun
        
        if df[cat_col].nunique() < 10:  # Makul sayıda kategoriye sahipse
            plt.figure(figsize=(12, 6))
            sns.boxplot(x=cat_col, y=num_col, data=df)
            plt.title(f'{cat_col} - {num_col} İlişkisi')
            plt.xlabel(cat_col)
            plt.ylabel(num_col)
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.savefig(f'{output_dir}/{cat_col}_{num_col}_iliskisi.png')
            plt.close()
            
            print(f"{cat_col} kategorilerine göre {num_col} ortalaması:")
            print(df.groupby(cat_col)[num_col].mean().sort_values(ascending=False))
    except Exception as e:
        print(f"Kategorik-sayısal ilişki analizinde hata: {e}")

# 5. Zaman serisi analizi (tarih sütunu varsa)
if len(date_columns) > 0 and len(numeric_columns) > 0:
    try:
        print("\nZaman serisi analizi yapılıyor...")
        date_col = date_columns[0]  # İlk tarih sütunu
        num_col = numeric_columns[0]  # İlk sayısal sütun
        
        # Tarihe göre gruplama
        time_series = df.groupby(pd.Grouper(key=date_col, freq='M'))[num_col].mean().reset_index()
        
        plt.figure(figsize=(14, 6))
        plt.plot(time_series[date_col], time_series[num_col], marker='o', linestyle='-')
        plt.title(f'Aylara Göre {num_col} Trendi')
        plt.xlabel('Tarih')
        plt.ylabel(num_col)
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.tight_layout()
        plt.savefig(f'{output_dir}/zaman_serisi_{num_col}.png')
        plt.close()
        
        print(f"Tarih sütunu {date_col}'a göre {num_col} zaman serisi analizi tamamlandı.")
    except Exception as e:
        print(f"Zaman serisi analizinde hata: {e}")

# 6. Aykırı değer analizi
print("\nAykırı değer analizi yapılıyor...")
for col in numeric_columns[:3]:  # İlk 3 sayısal sütun için aykırı değer analizi
    try:
        q1 = df[col].quantile(0.25)
        q3 = df[col].quantile(0.75)
        iqr = q3 - q1
        outlier_count = df[(df[col] < q1 - 1.5 * iqr) | (df[col] > q3 + 1.5 * iqr)].shape[0]
        outlier_percent = outlier_count / df.shape[0] * 100
        
        plt.figure(figsize=(10, 6))
        sns.boxplot(x=df[col])
        plt.title(f'{col} Aykırı Değer Analizi')
        plt.xlabel(col)
        plt.tight_layout()
        plt.savefig(f'{output_dir}/{col}_aykiri_deger.png')
        plt.close()
        
        print(f"{col} sütunu için aykırı değer sayısı: {outlier_count} (%{outlier_percent:.2f})")
    except Exception as e:
        print(f"{col} sütunu için aykırı değer analizinde hata: {e}")

# 7. İstatistiksel analizler
if len(numeric_columns) > 0 and len(categorical_columns) > 0:
    try:
        print("\nİstatistiksel analizler yapılıyor...")
        cat_col = categorical_columns[0]
        num_col = numeric_columns[0]
        
        if df[cat_col].nunique() <= 5:  # Makul sayıda kategori varsa
            categories = df[cat_col].unique()
            
            plt.figure(figsize=(12, 6))
            for category in categories:
                sns.kdeplot(df[df[cat_col] == category][num_col].dropna(), label=str(category))
            
            plt.title(f'{cat_col} Kategorilerine Göre {num_col} Dağılımı')
            plt.xlabel(num_col)
            plt.ylabel('Yoğunluk')
            plt.legend()
            plt.tight_layout()
            plt.savefig(f'{output_dir}/{cat_col}_{num_col}_dagilimi.png')
            plt.close()
            
            print(f"{cat_col} kategorilerine göre {num_col} dağılımı analizi tamamlandı.")
    except Exception as e:
        print(f"İstatistiksel analizlerde hata: {e}")

print("\n===== ANALİZ TAMAMLANDI =====")
print(f"Grafik ve analizler '{output_dir}' klasörüne kaydedildi.")

# Özet bulguları içeren bir rapor oluşturma
report_file = "xlsx_analiz_raporu.md"

with open(report_file, "w", encoding="utf-8") as f:
    f.write("# EXCEL VERİ SETİ ANALİZ RAPORU\n\n")
    
    f.write("## 1. VERİ SETİ GENEL BİLGİLERİ\n\n")
    f.write(f"**Veri Seti Boyutu**: {df.shape[0]} satır, {df.shape[1]} sütun\n\n")
    
    f.write("**Sütunlar**:\n")
    for col in df.columns:
        f.write(f"- {col}: {df[col].dtype}\n")
    
    f.write("\n**Eksik Değerler**:\n")
    missing_info = missing_df[missing_df['Eksik Değer Sayısı'] > 0]
    if not missing_info.empty:
        for idx, row in missing_info.iterrows():
            f.write(f"- {idx}: {row['Eksik Değer Sayısı']} kayıt (%{row['Yüzde (%)']:.2f})\n")
    else:
        f.write("- Veri setinde eksik değer bulunmamaktadır.\n")
    
    f.write("\n## 2. TEMEL ANALİZLER\n\n")
    
    if len(categorical_columns) > 0:
        f.write("### Kategorik Değişken Analizleri\n\n")
        for col in categorical_columns[:3]:  # İlk 3 kategorik sütun
            if df[col].nunique() < 20:
                f.write(f"**{col}** sütunu için en sık görülen değerler:\n")
                value_counts = df[col].value_counts().head(5)
                for val, count in value_counts.items():
                    f.write(f"- {val}: {count} (%{count/df.shape[0]*100:.2f})\n")
                f.write("\n")
    
    if len(numeric_columns) > 0:
        f.write("### Sayısal Değişken Analizleri\n\n")
        for col in numeric_columns[:3]:  # İlk 3 sayısal sütun
            f.write(f"**{col}** sütunu istatistikleri:\n")
            f.write(f"- Minimum: {df[col].min()}\n")
            f.write(f"- Maksimum: {df[col].max()}\n")
            f.write(f"- Ortalama: {df[col].mean()}\n")
            f.write(f"- Medyan: {df[col].median()}\n")
            f.write(f"- Standart Sapma: {df[col].std()}\n\n")
    
    if len(numeric_columns) > 1:
        f.write("### Korelasyon Analizi\n\n")
        f.write("Önemli korelasyonlar (mutlak değeri 0.3'ten büyük olanlar):\n")
        if 'important_corr' in locals() and not important_corr.empty:
            for idx, val in important_corr.items():
                f.write(f"- {idx[0]} ve {idx[1]}: {val:.3f}\n")
        else:
            f.write("- Güçlü korelasyon bulunamadı.\n")
    
    f.write("\n## 3. SONUÇ VE ÖNERİLER\n\n")
    f.write("Bu analiz, veri setinin yapısı ve içeriği hakkında temel içgörüler sunmaktadır. ")
    f.write("Daha detaylı analizler için 'analiz_sonuclari_xlsx' klasöründeki grafikleri inceleyebilirsiniz.\n\n")
    
    f.write("**Önerilen İleri Analizler**:\n")
    f.write("- Bulguları doğrulamak için daha detaylı istatistiksel testler yapılması\n")
    f.write("- Verinin daha temiz hale getirilmesi ve eksik değerlerin işlenmesi\n")
    f.write("- Kategori ve sayısal değişkenler arasındaki ilişkilerin daha detaylı incelenmesi\n")
    
    print(f"\nRapor '{report_file}' dosyasına kaydedildi.") 