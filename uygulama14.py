sayilar=[3,5,7,2,12,32,45]
toplam=0
for x in sayilar:
    toplam=toplam+x

    if x%3==0:
        print(x)
print(toplam)


# ürünler listesinde tüm iphone marka ürünleri listeleyiniz
urunler=["samsung s24","samsung s23","iphone 15","iphone 14"]

for i in urunler:
    index=i.find('iphone')
    if index >-1:
        print(i)
l=0
for j in urunler:
    inde=j.find('samsung')
    if inde>-1:
        l=l+1
print(l)



