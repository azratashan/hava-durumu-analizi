# IMDb Film Analizi Projesi

**Kısa Açıklama:**
Bu proje, IMDb verileri kullanılarak film analizi yapmak amacıyla hazırlanmış basit bir çalışma dizinidir. Ana betik `imdb-filmanalizi.py` olup, başlangıç veri seti `movies_initial.csv` içindedir.

**İçindekiler:**
- **Proje:** Kısa amaç ve kapsam
- **Gereksinimler:** Python sürümü ve önerilen paketler
- **Kurulum:** Ortam oluşturma ve gerekli paketlerin yüklenmesi
- **Kullanım:** Betiğin nasıl çalıştırılacağı
- **Veri:** `movies_initial.csv` hakkında kısa bilgi
- **Katkıda Bulunma:** Nasıl katkıda bulunulur
- **Lisans:** Kısa lisans bilgisi

**Gereksinimler:**
- Python 3.8 veya üstü
- Önerilen paketler: `pandas`, `numpy`, `matplotlib`, `seaborn` (betiğinizde farklı paketler kullanıldıysa buna göre güncelleyin)

**Kurulum:**
Aşağıdaki adımlar Windows PowerShell üzerinde örnektir.

```powershell
# (Opsiyonel) Sanal ortam oluşturma
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# Gerekli paketleri yükleyin (örnek)
pip install pandas numpy matplotlib seaborn
```

Eğer proje için bir `requirements.txt` dosyası eklerseniz, şu şekilde yükleyebilirsiniz:

```powershell
pip install -r requirements.txt
```

**Kullanım:**
Betiği çalıştırmak için proje klasöründe şu komutu kullanın:

```powershell
python imdb-filmanalizi.py
```

Betiğin `movies_initial.csv` dosyasını okuyup analizler/çizimler oluşturduğunu varsayarsanız, çalıştırmadan önce CSV dosyasının aynı klasörde bulunduğundan emin olun.

**Veri:**
- `movies_initial.csv`: Projede yer alan başlangıç veri setidir. İçeriği film başlığı, yıl, tür, puan vb. sütunlar içerebilir. (CSV içeriğini gözden geçirip gerekli açıklamaları buraya ekleyin.)

**Katkıda Bulunma:**
- Yeni analizler, görselleştirmeler veya veri temizleme adımları eklemek isterseniz bir `fork` oluşturup değişikliklerinizi `pull request` ile gönderebilirsiniz.
- Lütfen kodu çalıştırmadan önce gerekli paketleri yükleyin ve betiğin beklediği CSV sütunlarının varlığını doğrulayın.

**Lisans:**
Bu proje için açık bir lisans yoksa, kullanım ve paylaşım koşullarını belirtin. Örnek: MIT lisansı eklemek isterseniz `LICENSE` dosyası oluşturun.

---

Hazırladığım bu `README.md` temel bir şablondur. İsterseniz proje özelinde `Veri sütun açıklamaları`, `örnek çıktı görselleri`, veya `requirements.txt` dosyası ekleyip daha ayrıntılı hale getirebilirim.

