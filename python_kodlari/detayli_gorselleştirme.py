import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
from datetime import datetime

# Çıktı dizinini oluştur
output_dir = "detayli_gorseller"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Veri setini yükle
print("Veri seti yükleniyor...")
df = pd.read_excel("proje.xlsx")
print(f"Veri seti yüklendi: {df.shape[0]} satır, {df.shape[1]} sütun")

# Temel veri temizleme ve veri tipleri düzenleme
# Tarih sütununu tarih formatına dönüştür
df['Purchase Date'] = pd.to_datetime(df['Purchase Date'])

# Veri seti hakkında genel bilgi
print("\nVeri seti özeti:")
print(df.info())

# Eksik değerleri kontrol et
print("\nEksik Değerler:")
missing_values = df.isnull().sum()
missing_percentages = (missing_values / len(df)) * 100
missing_info = pd.DataFrame({
    'Eksik Değer Sayısı': missing_values,
    'Eksik Değer Yüzdesi': missing_percentages
})
print(missing_info[missing_info['Eksik Değer Sayısı'] > 0])

# Temel istatistikler
print("\nTemel İstatistikler:")
numeric_columns = df.select_dtypes(include=[np.number]).columns
print(df[numeric_columns].describe())

# Detaylı Görselleştirmeler
print("\nDetaylı görselleştirmeler oluşturuluyor...")

# 1. Zaman İçinde Toplam Satış Tutarı
plt.figure(figsize=(14, 7))
df_time = df.groupby(df['Purchase Date'].dt.to_period('M')).agg({
    'Total Purchase Amount': 'sum'
}).reset_index()
df_time['Purchase Date'] = df_time['Purchase Date'].dt.to_timestamp()

plt.plot(df_time['Purchase Date'], df_time['Total Purchase Amount'], marker='o', linestyle='-')
plt.title('Aylara Göre Toplam Satış Tutarı', fontsize=16)
plt.xlabel('Tarih', fontsize=12)
plt.ylabel('Toplam Satış Tutarı (TL)', fontsize=12)
plt.grid(True, alpha=0.3)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(f"{output_dir}/aylik_satis_tutari.png")
plt.close()

# 2. Ürün Kategorilerine Göre Satış Dağılımı (Pasta Grafiği)
plt.figure(figsize=(10, 10))
category_sales = df.groupby('Product Category')['Total Purchase Amount'].sum()
plt.pie(category_sales, labels=category_sales.index, autopct='%1.1f%%', startangle=90, shadow=True)
plt.title('Kategorilere Göre Toplam Satış Tutarı Dağılımı', fontsize=16)
plt.axis('equal')
plt.tight_layout()
plt.savefig(f"{output_dir}/kategori_satis_dagilimi.png")
plt.close()

# 3. Ödeme Yöntemlerine Göre Satış Sayıları (Yatay Bar Grafiği)
plt.figure(figsize=(12, 6))
payment_counts = df['Payment Method'].value_counts()
sns.barplot(x=payment_counts.values, y=payment_counts.index, palette='viridis')
plt.title('Ödeme Yöntemlerine Göre Satış Sayıları', fontsize=16)
plt.xlabel('Satış Sayısı', fontsize=12)
plt.ylabel('Ödeme Yöntemi', fontsize=12)
plt.tight_layout()
plt.savefig(f"{output_dir}/odeme_yontemi_satis.png")
plt.close()

# 4. Yaş Gruplarına Göre Satın Alma Tutarı Dağılımı
plt.figure(figsize=(14, 7))
# Yaş grupları oluştur
df['Age Group'] = pd.cut(df['Age'], bins=[17, 25, 35, 45, 55, 75], labels=['18-25', '26-35', '36-45', '46-55', '56+'])
age_purchase = df.groupby('Age Group')['Total Purchase Amount'].mean().reset_index()

sns.barplot(x='Age Group', y='Total Purchase Amount', data=age_purchase, palette='Blues_d')
plt.title('Yaş Gruplarına Göre Ortalama Satın Alma Tutarı', fontsize=16)
plt.xlabel('Yaş Grubu', fontsize=12)
plt.ylabel('Ortalama Satın Alma Tutarı (TL)', fontsize=12)
plt.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.savefig(f"{output_dir}/yas_grubu_ortalama_tutar.png")
plt.close()

# 5. Cinsiyete Göre Kategori Tercihleri
plt.figure(figsize=(14, 8))
gender_category = df.groupby(['Gender', 'Product Category']).size().unstack()
gender_category.plot(kind='bar', stacked=False)
plt.title('Cinsiyete Göre Ürün Kategorisi Tercihleri', fontsize=16)
plt.xlabel('Cinsiyet', fontsize=12)
plt.ylabel('Satın Alma Sayısı', fontsize=12)
plt.xticks(rotation=0)
plt.legend(title='Ürün Kategorisi', fontsize=10)
plt.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.savefig(f"{output_dir}/cinsiyet_kategori_tercihleri.png")
plt.close()

# 6. İade Oranları ve Analizi
plt.figure(figsize=(12, 7))
# İade sütunundaki eksik değerleri 'No' olarak doldur (eğer gerekirse)
if df['Returns'].isna().any():
    df['Returns_Filled'] = df['Returns'].fillna('No')
else:
    df['Returns_Filled'] = df['Returns']

returns_by_category = df.groupby(['Product Category', 'Returns_Filled']).size().unstack(fill_value=0)
if 'Yes' in returns_by_category.columns:
    returns_by_category['Return Rate'] = returns_by_category['Yes'] / (returns_by_category['Yes'] + returns_by_category['No']) * 100

    returns_by_category['Return Rate'].plot(kind='bar', color='red')
    plt.title('Ürün Kategorilerine Göre İade Oranları', fontsize=16)
    plt.xlabel('Ürün Kategorisi', fontsize=12)
    plt.ylabel('İade Oranı (%)', fontsize=12)
    plt.grid(True, alpha=0.3, axis='y')
    plt.tight_layout()
    plt.savefig(f"{output_dir}/kategori_iade_oranlari.png")
    plt.close()

# 7. Müşteri Ayrılma (Churn) Analizi
plt.figure(figsize=(10, 6))
churn_counts = df['Churn'].value_counts()
labels = ['Devam Eden', 'Ayrılan']
colors = ['green', 'red']

plt.pie(churn_counts, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90, shadow=True)
plt.title('Müşteri Ayrılma (Churn) Oranı', fontsize=16)
plt.axis('equal')
plt.tight_layout()
plt.savefig(f"{output_dir}/musteri_ayrilma_orani.png")
plt.close()

# 8. Korelasyon Matrisi - Isı Haritası
plt.figure(figsize=(12, 10))
corr_columns = ['Customer ID', 'Product Price', 'Quantity', 'Total Purchase Amount', 'Age', 'Churn']
corr_matrix = df[corr_columns].corr()

sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Değişkenler Arası Korelasyon Matrisi', fontsize=16)
plt.tight_layout()
plt.savefig(f"{output_dir}/korelasyon_matrisi.png")
plt.close()

# 9. Kutu Grafiği - Fiyat Dağılımı (Kategorilere Göre)
plt.figure(figsize=(14, 8))
sns.boxplot(x='Product Category', y='Product Price', data=df)
plt.title('Ürün Kategorilerine Göre Fiyat Dağılımı', fontsize=16)
plt.xlabel('Ürün Kategorisi', fontsize=12)
plt.ylabel('Ürün Fiyatı (TL)', fontsize=12)
plt.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.savefig(f"{output_dir}/kategori_fiyat_dagilimi.png")
plt.close()

# 10. Çizgi + Çubuk Grafiği - Kategori ve Zaman Bazlı Trend
plt.figure(figsize=(16, 8))
df['Month'] = df['Purchase Date'].dt.to_period('M')
category_time = df.groupby(['Month', 'Product Category'])['Total Purchase Amount'].sum().unstack()
category_time.index = category_time.index.to_timestamp()

ax = category_time.plot(kind='bar', stacked=True, figsize=(16, 8))
plt.title('Aylara ve Kategorilere Göre Toplam Satış Tutarı', fontsize=16)
plt.xlabel('Ay', fontsize=12)
plt.ylabel('Toplam Satış Tutarı (TL)', fontsize=12)
plt.legend(title='Ürün Kategorisi', fontsize=10)
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.savefig(f"{output_dir}/aylik_kategori_satis.png")
plt.close()

# 11. İade Durumuna Göre Kutu Grafiği
plt.figure(figsize=(12, 7))
if 'Returns_Filled' in df.columns:
    sns.boxplot(x='Returns_Filled', y='Total Purchase Amount', data=df)
    plt.title('İade Durumuna Göre Toplam Satın Alma Tutarı Dağılımı', fontsize=16)
    plt.xlabel('İade Durumu', fontsize=12)
    plt.ylabel('Toplam Satın Alma Tutarı (TL)', fontsize=12)
    plt.grid(True, alpha=0.3, axis='y')
    plt.tight_layout()
    plt.savefig(f"{output_dir}/iade_tutar_dagilimi.png")
    plt.close()

# 12. Yoğunluk Haritası - Yaş ve Satın Alma Tutarı İlişkisi
plt.figure(figsize=(14, 8))
sns.kdeplot(data=df, x='Age', y='Total Purchase Amount', cmap='viridis', fill=True)
plt.title('Yaş ve Toplam Satın Alma Tutarı İlişkisi', fontsize=16)
plt.xlabel('Yaş', fontsize=12)
plt.ylabel('Toplam Satın Alma Tutarı (TL)', fontsize=12)
plt.tight_layout()
plt.savefig(f"{output_dir}/yas_tutar_iliskisi.png")
plt.close()

print(f"\nTüm görselleştirmeler '{output_dir}' klasörüne kaydedildi.") 