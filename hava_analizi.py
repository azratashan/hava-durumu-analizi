import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# --- AŞAMA 1: VERİ YÜKLEME VE HAZIRLIK (Noktalı Virgül (;) Hatası Düzeltildi) ---

# 1. Veri Setini Yükleme
try:
    # sep=';' parametresini ekleyerek dosyanın doğru ayrılmasını sağlıyoruz.
    df = pd.read_csv('munich.csv', sep=';') 
    print("Veri seti başarıyla yüklendi.")
except FileNotFoundError:
    print("HATA: Dosya bulunamadı. Lütfen dosya adını ve yolunu kontrol edin.")
    
# 2. Tarih Sütununu Düzeltme (Hata çözüldü, satırı tekrar açtık)
df['time'] = pd.to_datetime(df['time'])

# 3. İlk Veri Keşfi ve Kontrol
print("\n--- İlk 5 Satır ---")
print(df.head()) 

print("\n--- Veri Seti Bilgi Özeti ---")
df.info() # Veri tiplerini, eksik veri sayısını gösterir