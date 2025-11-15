import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


try:
    
    df = pd.read_csv('munich.csv', sep=';') 
    print("Veri seti başarıyla yüklendi.")
except FileNotFoundError:
    print("HATA: Dosya bulunamadı. Lütfen dosya adını ve yolunu kontrol edin.")
    

df['time'] = pd.to_datetime(df['time'])


print("\n--- İlk 5 Satır ---")
print(df.head()) 

print("\n--- Veri Seti Bilgi Özeti ---")
df.info() 

df['precipitation_sum (mm)'] = df['precipitation_sum (mm)'].fillna(0)
df['snowfall_sum (cm)'] = df['snowfall_sum (cm)'].fillna(0)


print("\n--- Eksik Veri Doldurulduktan Sonraki Kontrol ---")
df.info()


df['year'] = df['time'].dt.year


yillik_ortalama = df.groupby('year')['precipitation_sum (mm)'].mean()

print("\n--- Yıllık Ortalama Yağış Miktarları ---")
print(yillik_ortalama)


df['month'] = df['time'].dt.month


aylik_ortalama = df.groupby('month')[['precipitation_sum (mm)', 'snowfall_sum (cm)']].mean()


plt.figure(figsize=(10, 6))


plt.plot(aylik_ortalama.index, aylik_ortalama['precipitation_sum (mm)'], 
         marker='o', linestyle='-', color='skyblue', label='Ortalama Yağış (mm)')


plt.plot(aylik_ortalama.index, aylik_ortalama['snowfall_sum (cm)'], 
         marker='x', linestyle='--', color='darkblue', label='Ortalama Kar (cm)')

plt.title('2024 Yılı Aylık Ortalama Yağış ve Kar Miktarları')
plt.xlabel('Ay')
plt.ylabel('Miktar (mm/cm)')
plt.xticks(aylik_ortalama.index) 
plt.legend()
plt.grid(True)
plt.show()