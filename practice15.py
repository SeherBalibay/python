urunler=[
    {"urunAdi":"Hp Victus","fiyat":32999},
    {"urunAdi":"Lenova ThinkPad","fiyat":25499},
    {"urunAdi":"Aple Mackbook","fiyat":49999},
    {"urunAdi":"Huawei Matebook","fiyat":26999},
    {"urunAdi":"Casper Nirvana","fiyat":20000}
]

for urun in urunler:
    print(f"{urun["urunAdi"]} marka ürünün fiyatı {urun["fiyat"]} Türk lirasıdır")
toplam=0

for urunx in urunler:
    toplam=toplam+urunx["fiyat"]
print(toplam)

for uruny in urunler:
    if (uruny["fiyat"]>=25000 and uruny["fiyat"]<=40000):
        print(uruny["urunAdi"])

kelime=input("anahtar kelime giriniz: ")
for urun in urunler:
    if urun["urunAdi"].lower().find(kelime.lower()) >-1:
        print(urun["urunAdi"])



