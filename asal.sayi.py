asal=True
sayi=int(input("Lütfen bir sayı giriniz: "))  

if (sayi <= 1):
  print("Birden büyük bir sayı giriniz.")  
else:
  for i in range(2,sayi):
    if (sayi % i == 0):
      asal=False
      break
    else:
      continue
      
  if(asal==True)):
    print( "Bu bir asal sayıdır")
  else:
    print("Bu bir asal sayı değildir")