import matplotlib.pyplot as plt
def olustur_sihirli_kare(A, B, C, D):
    # 4x4 bir ızgara oluştur
    sihirli_kare = [[0] * 4 for _ in range(4)]

    # Verilen modele göre kareyi doldur
    sihirli_kare[0] = [A, B, C, D]
    sihirli_kare[1] = [D + 1, C - 1, B - 3, A + 3]
    sihirli_kare[2] = [B - 2, A + 2, D + 2, C - 2]
    sihirli_kare[3] = [C + 1, D - 1, A + 1, B - 1]

    return sihirli_kare

def sihirli_kareyi_goster(sihirli_kare, dogum_tarihi):
    # Kare hücreleriyle sihirli kareyi görselleştir
    fig, ax = plt.subplots()
    ax.axis('tight')
    ax.axis('off')

    # Kare hücreleriyle bir tablo oluştur
    table = ax.table(cellText=sihirli_kare, cellLoc='center', loc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(12)

    # Hücre yüksekliğini ve genişliğini eşit yaparak kare yap
    for i in range(4):
        for j in range(4):
            table[(i, j)].set_height(0.2)
            table[(i, j)].set_width(0.2)

    # Doğum tarihini sol üst köşeye ekle
    ax.text(0.1, 0.95, f"Doğum Tarihi: {dogum_tarihi}", fontsize=12, transform=ax.transAxes)

    return fig, ax, table

def toplamlari_goster(sihirli_kare, ax, table):
    # Sağdan sola her sütunun toplamını hesapla
    sagdan_sola_toplamlar = [sum(col) for col in zip(*sihirli_kare[::-1])]

    # Yukarıdan aşağı her sütunun toplamını hesapla
    yukaridan_asagi_toplamlar = [sum(row) for row in sihirli_kare]

    # Toplamları sihirli karenin sağına ekle
    for i, toplam in enumerate(sagdan_sola_toplamlar):
        ax.text(0.95, 0.8 - i * 0.2, f'=   Toplam: {toplam}', fontsize=12, transform=ax.transAxes)

    # Toplamları sihirli karenin altına ekle
    for j, toplam in enumerate(yukaridan_asagi_toplamlar):
        ax.text(0.16 + j * 0.2, 0.0, f'Toplam: {toplam}', fontsize=12, transform=ax.transAxes)

    return sagdan_sola_toplamlar, yukaridan_asagi_toplamlar

# Verilen Dogum Tarihi Sayıları.A-B-C-D kısımlarına kendi dogum tarihi sayılarınızı yazın.
A = 22
B = 12
C = 18
D = 87
dogum_tarihi = "22 12 1887" # Buraya dogum tarihinizi yazın.
sihirli_kare = olustur_sihirli_kare(A, B, C, D)

# Sihirli kareyi göster
fig, ax, table = sihirli_kareyi_goster(sihirli_kare, dogum_tarihi)

# Toplamları göster ve sonuçları al
sagdan_sola_toplamlar, yukaridan_asagi_toplamlar = toplamlari_goster(sihirli_kare, ax, table)

# Tüm toplamların eşit olup olmadığını kontrol et
tum_toplamlar_esit_mi = all(toplam == sagdan_sola_toplamlar[0] for toplam in sagdan_sola_toplamlar + yukaridan_asagi_toplamlar)



plt.show()
