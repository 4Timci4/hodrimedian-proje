import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import os

# Çıktı dizinini oluştur
output_dir = "rfm_analiz_sonuclari"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Veri setini yükle
print("Veri seti yükleniyor...")
df = pd.read_excel("proje.xlsx")
print(f"Veri seti yüklendi: {df.shape[0]} satır, {df.shape[1]} sütun")

# Tarih sütununu tarih formatına dönüştür
df['Purchase Date'] = pd.to_datetime(df['Purchase Date'])

# Analiz tarihi olarak veri setindeki en son tarihi alalım ve 1 gün ekleyelim
analysis_date = df['Purchase Date'].max() + pd.Timedelta(days=1)
print(f"Analiz tarihi: {analysis_date}")

# RFM Değerleri Hesaplama
# Müşteri bazında gruplama yaparak RFM değerlerini hesaplayalım
rfm = df.groupby('Customer ID').agg({
    'Purchase Date': lambda x: (analysis_date - x.max()).days,  # Recency
    'Customer ID': 'count',  # Frequency
    'Total Purchase Amount': 'sum'  # Monetary
})

# Sütun isimlerini düzenleyelim
rfm.columns = ['Recency', 'Frequency', 'Monetary']

# İstatistikleri görelim
print("\nRFM İstatistikleri:")
print(rfm.describe())

# RFM skorları için çeyreklikleri hesaplayalım
# Recency için düşük değerler daha iyidir (daha yakın zamanda alışveriş)
r_quartiles = pd.qcut(rfm['Recency'], 4, labels=range(4, 0, -1))

# Frequency ve Monetary için yüksek değerler daha iyidir
f_quartiles = pd.qcut(rfm['Frequency'], 4, labels=range(1, 5))
m_quartiles = pd.qcut(rfm['Monetary'], 4, labels=range(1, 5))

# RFM çeyreklik değerlerini ana veri setine ekleyelim
rfm['R'] = r_quartiles
rfm['F'] = f_quartiles
rfm['M'] = m_quartiles

# R, F ve M skorlarının birleşimi olarak RFM skoru oluşturalım
rfm['RFM_Score'] = rfm['R'].astype(str) + rfm['F'].astype(str) + rfm['M'].astype(str)

# RFM segmentleri oluşturalım
def segment_rfm(r, f, m):
    if r >= 3 and f >= 3 and m >= 3:
        return 'Champions'
    elif (r >= 2 and r < 4) and (f >= 3) and (m >= 3):
        return 'Loyal Customers'
    elif (r >= 3) and (f >= 1 and f < 3) and (m >= 2):
        return 'Potential Loyalists'
    elif (r >= 4) and (f >= 1) and (m >= 1):
        return 'New Customers'
    elif (r >= 3) and (f >= 1 and f < 3) and (m < 2):
        return 'Promising'
    elif (r >= 2 and r < 4) and (f < 3) and (m >= 2 and m < 4):
        return 'Customers Needing Attention'
    elif (r >= 2 and r < 4) and (f < 3) and (m < 2):
        return 'About to Sleep'
    elif r < 2 and f >= 2 and m >= 2:
        return 'At Risk'
    elif r < 2 and f >= 2 and m < 2:
        return 'Cant Lose Them'
    elif r < 2 and f < 2 and m >= 2:
        return 'Hibernating'
    else:
        return 'Lost'

# R, F ve M değerlerini sayısal değerlere dönüştürelim
rfm['R'] = rfm['R'].astype(int)
rfm['F'] = rfm['F'].astype(int)
rfm['M'] = rfm['M'].astype(int)

# Segment ataması yapalım
rfm['Segment'] = rfm.apply(lambda x: segment_rfm(x['R'], x['F'], x['M']), axis=1)

# Segmentlerin boyut ve yüzdelerini hesaplayalım
segment_counts = rfm['Segment'].value_counts().reset_index()
segment_counts.columns = ['Segment', 'Count']
segment_counts['Percentage'] = segment_counts['Count'] / segment_counts['Count'].sum() * 100

print("\nSegment Dağılımı:")
print(segment_counts)

# Segmentlerin ortalama RFM değerlerini görelim
segment_averages = rfm.groupby('Segment').agg({
    'Recency': 'mean',
    'Frequency': 'mean',
    'Monetary': 'mean'
}).reset_index()

print("\nSegment Ortalama Değerleri:")
print(segment_averages)

# Görselleştirmeler

# 1. Segment Dağılımı (Pasta Grafiği)
plt.figure(figsize=(12, 8))
plt.pie(segment_counts['Count'], labels=segment_counts['Segment'], autopct='%1.1f%%', startangle=90, shadow=True)
plt.title('Müşteri Segmentleri Dağılımı', fontsize=16)
plt.axis('equal')
plt.tight_layout()
plt.savefig(f"{output_dir}/segment_dagilim.png")
plt.close()

# 2. Segment Bazlı Ortalama Recency, Frequency ve Monetary (Bar Grafiği)
fig, axes = plt.subplots(3, 1, figsize=(14, 18))

# Recency
sns.barplot(x='Segment', y='Recency', data=segment_averages, ax=axes[0], palette='Blues_d')
axes[0].set_title('Segmentlere Göre Ortalama Recency (Gün)', fontsize=14)
axes[0].set_xticklabels(axes[0].get_xticklabels(), rotation=45, ha='right')
axes[0].grid(True, alpha=0.3, axis='y')

# Frequency
sns.barplot(x='Segment', y='Frequency', data=segment_averages, ax=axes[1], palette='Greens_d')
axes[1].set_title('Segmentlere Göre Ortalama Frequency (İşlem Sayısı)', fontsize=14)
axes[1].set_xticklabels(axes[1].get_xticklabels(), rotation=45, ha='right')
axes[1].grid(True, alpha=0.3, axis='y')

# Monetary
sns.barplot(x='Segment', y='Monetary', data=segment_averages, ax=axes[2], palette='Reds_d')
axes[2].set_title('Segmentlere Göre Ortalama Monetary (Toplam Harcama)', fontsize=14)
axes[2].set_xticklabels(axes[2].get_xticklabels(), rotation=45, ha='right')
axes[2].grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.savefig(f"{output_dir}/segment_rfm_ortalama.png")
plt.close()

# 3. Segmentlerin 3D Scatter Plot
fig = plt.figure(figsize=(14, 10))
ax = fig.add_subplot(111, projection='3d')

# Renk haritası oluştur
segments = rfm['Segment'].unique()
colors = plt.cm.tab20(np.linspace(0, 1, len(segments)))
segment_color_map = dict(zip(segments, colors))

# Her segment için ayrı ayrı nokta çiz
for segment in segments:
    segment_data = rfm[rfm['Segment'] == segment]
    ax.scatter(segment_data['Recency'], 
               segment_data['Frequency'], 
               segment_data['Monetary'],
               c=[segment_color_map[segment]],
               label=segment,
               alpha=0.7)

# Eksenleri ve başlığı ayarla
ax.set_xlabel('Recency (Gün)', fontsize=12)
ax.set_ylabel('Frequency (İşlem Sayısı)', fontsize=12)
ax.set_zlabel('Monetary (Toplam Harcama)', fontsize=12)
ax.set_title('Müşteri Segmentleri 3D Görünümü', fontsize=16)

# Eksenleri sınırla
ax.set_xlim(0, rfm['Recency'].max() * 1.1)
ax.set_ylim(0, rfm['Frequency'].max() * 1.1)
ax.set_zlim(0, rfm['Monetary'].max() * 1.1)

# Lejant
plt.legend(title='Segmentler', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
plt.savefig(f"{output_dir}/segment_3d_scatter.png")
plt.close()

# 4. Isı Haritası - Segment ve RFM Skorları
plt.figure(figsize=(16, 12))
pivot = pd.crosstab(index=rfm['R'].astype(str), 
                   columns=rfm['F'].astype(str) + rfm['M'].astype(str),
                   values=rfm['Segment'].map(segment_counts.set_index('Segment')['Count']),
                   aggfunc='sum').fillna(0)

sns.heatmap(pivot, cmap='viridis', annot=True, fmt='.0f', linewidths=0.5)
plt.title('RFM Skorları Isı Haritası (Hücre Değerleri: Müşteri Sayısı)', fontsize=16)
plt.xlabel('F-M Skoru (Frequency-Monetary)', fontsize=12)
plt.ylabel('R Skoru (Recency)', fontsize=12)
plt.tight_layout()
plt.savefig(f"{output_dir}/rfm_heatmap.png")
plt.close()

# 5. Pareto Grafiği - Segmentlerin Toplam Harcama İçindeki Payı
segment_monetary = rfm.groupby('Segment')['Monetary'].sum().reset_index()
segment_monetary = segment_monetary.sort_values('Monetary', ascending=False)
segment_monetary['Cumulative Percentage'] = segment_monetary['Monetary'].cumsum() / segment_monetary['Monetary'].sum() * 100

fig, ax1 = plt.subplots(figsize=(14, 8))

# Bar grafiği
bars = ax1.bar(segment_monetary['Segment'], segment_monetary['Monetary'], color='royalblue')
ax1.set_xlabel('Müşteri Segmenti', fontsize=12)
ax1.set_ylabel('Toplam Harcama', fontsize=12)
ax1.set_title('Segmentlerin Toplam Harcama İçindeki Payı - Pareto Analizi', fontsize=16)
ax1.set_xticklabels(ax1.get_xticklabels(), rotation=45, ha='right')

# Kümülatif yüzde için ikinci y ekseni
ax2 = ax1.twinx()
ax2.plot(segment_monetary['Segment'], segment_monetary['Cumulative Percentage'], 'ro-', linewidth=2)
ax2.set_ylabel('Kümülatif Yüzde (%)', fontsize=12)
ax2.set_ylim(0, 110)

# 20-80 çizgisi
ax2.axhline(y=80, color='green', linestyle='--', alpha=0.7)
ax2.text(0, 81, '80% Gelir', fontsize=10, color='green')

plt.tight_layout()
plt.savefig(f"{output_dir}/segment_pareto.png")
plt.close()

# 6. Her segmentin ürün kategorisi tercihleri
# Original veri setiyle RFM sonuçlarını birleştirelim
rfm_with_customerid = rfm.reset_index()
df_with_segment = pd.merge(df, rfm_with_customerid[['Customer ID', 'Segment']], on='Customer ID', how='left')

# Segmentlere göre ürün kategorisi tercihleri
segment_category = df_with_segment.groupby(['Segment', 'Product Category']).size().unstack().fillna(0)

# Yüzdeleri hesaplayalım
segment_category_percent = segment_category.div(segment_category.sum(axis=1), axis=0) * 100

plt.figure(figsize=(16, 10))
segment_category_percent.plot(kind='bar', stacked=True)
plt.title('Müşteri Segmentlerine Göre Ürün Kategorisi Tercihleri (%)', fontsize=16)
plt.xlabel('Müşteri Segmenti', fontsize=12)
plt.ylabel('Yüzde (%)', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.legend(title='Ürün Kategorisi', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig(f"{output_dir}/segment_kategori_tercihleri.png")
plt.close()

# 7. Segment bazlı iade oranları
if 'Returns' in df_with_segment.columns:
    # Eksik değerleri dolduralım
    df_with_segment['Returns_Filled'] = df_with_segment['Returns'].fillna('No')
    
    # Segmentlere göre iade oranları
    segment_returns = df_with_segment.groupby(['Segment', 'Returns_Filled']).size().unstack().fillna(0)
    
    if 'Yes' in segment_returns.columns and 'No' in segment_returns.columns:
        segment_returns['Return Rate'] = segment_returns['Yes'] / (segment_returns['Yes'] + segment_returns['No']) * 100
        
        plt.figure(figsize=(14, 8))
        segment_returns['Return Rate'].sort_values(ascending=False).plot(kind='bar', color='red')
        plt.title('Müşteri Segmentlerine Göre İade Oranları', fontsize=16)
        plt.xlabel('Müşteri Segmenti', fontsize=12)
        plt.ylabel('İade Oranı (%)', fontsize=12)
        plt.xticks(rotation=45, ha='right')
        plt.grid(True, alpha=0.3, axis='y')
        plt.tight_layout()
        plt.savefig(f"{output_dir}/segment_iade_oranlari.png")
        plt.close()

# RFM segmentlerini CSV dosyasına kaydet
rfm.reset_index().to_csv(f"{output_dir}/rfm_segmentler.csv", index=False)

# Segment önerileri 
segment_recommendations = {
    'Champions': 'Sadakat programları, özel indirimler, VIP hizmetler sunulmalı.',
    'Loyal Customers': 'Düzenli iletişim ve özel ürün önerileri yapılmalı.',
    'Potential Loyalists': 'İletişimi artırarak sadakat programlarına dahil edilmeli.',
    'New Customers': 'Ürün satın alma deneyimlerini iyileştirmeye odaklanılmalı.',
    'Promising': 'Satın alma sıklığını artırmak için teşvikler sunulmalı.',
    'Customers Needing Attention': 'Dikkat çekici kampanyalar ile ilgi yeniden kazanılmalı.',
    'About to Sleep': 'Kaybetmeden önce özel tekliflerle tekrar kazanılmalı.',
    'At Risk': 'Acil win-back kampanyaları düzenlenmeli.',
    'Cant Lose Them': 'Kişiselleştirilmiş iletişim ve özel teklifler sunulmalı.',
    'Hibernating': 'Yeniden aktivasyon kampanyaları düzenlenmeli.',
    'Lost': 'Düşük maliyetli win-back kampanyaları veya pasif olarak bırakılmalı.'
}

# Segment önerilerini CSV dosyasına kaydet
recommendations_df = pd.DataFrame({
    'Segment': segment_recommendations.keys(),
    'Öneri': segment_recommendations.values()
})
recommendations_df.to_csv(f"{output_dir}/segment_onerileri.csv", index=False)

print(f"\nRFM analizi tamamlandı. Tüm sonuçlar '{output_dir}' klasörüne kaydedildi.")

# Segmentlere göre özet rapor oluştur
with open(f"{output_dir}/rfm_ozet_raporu.md", "w", encoding="utf-8") as f:
    f.write("# RFM ANALİZİ ÖZET RAPORU\n\n")
    
    f.write("## Segment Dağılımı\n\n")
    segment_counts['Percentage'] = segment_counts['Percentage'].round(2)
    segment_table = segment_counts.to_markdown(index=False)
    f.write(segment_table + "\n\n")
    
    f.write("## Segment Ortalama Değerleri\n\n")
    segment_averages_rounded = segment_averages.copy()
    segment_averages_rounded['Recency'] = segment_averages_rounded['Recency'].round(2)
    segment_averages_rounded['Frequency'] = segment_averages_rounded['Frequency'].round(2)
    segment_averages_rounded['Monetary'] = segment_averages_rounded['Monetary'].round(2)
    segment_avg_table = segment_averages_rounded.to_markdown(index=False)
    f.write(segment_avg_table + "\n\n")
    
    f.write("## Segment Önerileri\n\n")
    for segment, recommendation in segment_recommendations.items():
        f.write(f"### {segment}\n")
        f.write(f"{recommendation}\n\n")
    
    f.write("## Özet Bulgular\n\n")
    f.write("1. En değerli müşteriler Champions ve Loyal Customers segmentlerinde bulunmaktadır.\n")
    f.write("2. At Risk ve Hibernating segmentlerindeki müşteriler için acil müdahale gerekmektedir.\n")
    f.write("3. New Customers ve Potential Loyalists segmentlerindeki müşterilerin sadık müşterilere dönüştürülmesi için stratejiler geliştirilmelidir.\n")
    f.write("4. Champions segmenti toplam gelirin büyük bir kısmını oluşturmaktadır ve bu segmentin korunması kritik önem taşımaktadır.\n")
    
print(f"RFM özet raporu '{output_dir}/rfm_ozet_raporu.md' dosyasına kaydedildi.") 