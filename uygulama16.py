basla=int(input("başlangıç değeri: "))
bitis=int(input("bitiş değeri: "))

while basla<=bitis:
    print(basla)
    basla+=1

i=100

while i>=1:
    print(i)
    i-=1

#kullanıcıdan alacağınız 5 sayıyı ekranda sıralı bir şekilde yazdırın

i=0
list=[]

while (i<5):
    sayi=int(input("sayı: "))
    list.append(sayi)
    i+=1

list.sort()
print(list)

# klavyeden girişi istenen username bilgisi için boşluk girildiği sürece tekrar username girişi isteyiniz
#while username demek true olur while not username dersek false döndüür

username=""

while not username:
    username=input("kullanıcı adı:")

print("girilen username"+username)