kisi = {"isim": "ali", "yas": 20, "cinsiyet": "m", "hobiler": ["sinema", "konser", "yazılım"]}

print(kisi["isim"])
kisi.update({"isim": "Ahmet","yas":30})
print(kisi)

kisi["id"] = 1236
print(kisi)

del kisi["id"]
print(kisi)

for i in kisi:
    print(kisi[i])

print(kisi.keys())
print(kisi.values())
print(kisi.items())

for i in kisi.items():
    print(i)

for i,j in kisi.items():
        print(i,j)