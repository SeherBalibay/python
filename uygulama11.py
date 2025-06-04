benzinFiyat=39.35
dizelFiyat=41.71
lpgFiyat=20.28

toplamYakitUcreti=0
ortalamaYakitTuketimi= float(input("100 km de ortalama yakıt tüketimi"))
mesafe=float(input("gidilen yol"))
yakitTipi=input("Yakıt tipi: ")

toplamYakitTuketimi=mesafe*(ortalamaYakitTuketimi/100)


if (yakitTipi=="benzin"):
    toplamYakitUcreti=benzinFiyat*toplamYakitTuketimi

elif(yakitTipi=="dizel"):
    toplamYakitUcreti = dizelFiyat * toplamYakitTuketimi

elif(yakitTipi=="lpg"):
    toplamYakitUcreti = lpgFiyat * toplamYakitTuketimi

else:
    print("yanlış yakıt tipi")


if(toplamYakitUcreti!=0):
    print(toplamYakitUcreti)

