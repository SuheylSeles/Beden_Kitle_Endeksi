print("""

VÜCUT KİTLE ENDEKSİ HESAPLAMASI

""")

boy = float(input("Boyunuzu Giriniz: "))
kilo = int(input("Kilonuzu Giriniz: "))


bki = kilo / (boy**2)

if(bki > 30):
    print("Obez")
elif(bki>=25 and bki<=30):
    print("Fazla Kilolu")
elif(bki<25 and bki>18.5):
    print("Normal")
else:
    print("Zayıf")

