sayilar=[0,-10,20,45,7,78,25,9,23,-40]
for item in sayilar:
    print(item)
x=0
while(x<len(sayilar)):
   print(sayilar[x])
   x+=1
basla=int(input("Başlangıç:"))
bitiş=int(input("Bitiş:"))

while(basla<bitis):
  basla+=1
  if(basla %2 ==0):
     print("Çift sayılar =>",basla)