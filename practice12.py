ogrenciler=[]
devammi="e"
while devammi != "h":
    ogrenciNo=input()
    ogrenciAdi=input()
    ogrenciSoyad=input()

    ogrenciler.append({
        "ogrenciNo": ogrenciNo,
        "ogrenciAdi": ogrenciAdi,
        "ogrenciSoyad":ogrenciSoyad
    })
    devammi=input("devam mı? (e/h)")

for ogrenci in ogrenciler:
    print(f"{ogrenci["ogrenciNo"]} numaralı öğrencinin adı {ogrenci["ogrenciAdi"]}{ogrenci["ogrenciSoyad"]}")
