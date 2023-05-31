class Donto:
    def __init__(self, adatsor):
        reszletek = adatsor.split(";")
        #Adatmező kialakítása
        self.ssz = reszletek[0]
        self.datum = reszletek[1]
        self.gyoztes = reszletek[2]
        self.eredmeny = reszletek[3]
        self.vesztes = reszletek[4]
        self.helyszin = reszletek[5]
        self.varosallam = reszletek[6]
        self.nezoszam = int(reszletek[7])

def __str__(self):
    return f"{self.datum}, {self.helyszin}: {self.gyoztes} - {self.vesztes} ({self.eredmeny})"

def pontkulonbseg(self):
    reszletek = self.eredmeny.split('-')
    return int(reszletek[0]) - int(reszletek[1])
    


#0
print("Super Bowl döntőinek feldolgozása")

#1
finp = open("SuperBowl.txt", mode="rt", encoding="utf8")
adatsorok = finp.read().split('\n')
finp.close()

dontok = []
for i in range(1, len(adatsorok)):
    if adatsorok[i] != "":
        donto = Donto(adatsorok[i])
        dontok.append(donto)

for item in dontok:
    print(item)
print("----------------------------------------------------------------")

#programozási tételek
#Összegzés tétele
#Határozza meg hogy a SuperBowl döntöket hány ember látogatta meg!

#sum - határozza meg az adatok lista elemeinek összegét
sum = 0 
for item in dontok:
    sum += item.nezoszam
    print(f"sum= {sum}")
print("-------------------------------------------")

#átlag
#Határozza meg a látogatók átlagos számát
sum = 0
for item in dontok:
    sum += item.nezoszam
atlag = sum / len(dontok)
print(f"átlag = {atlag:.2f}")
print("-----------------------------------------------")

#min - max tétel
#min
#Határozza meg  hogy a döntök között milyen volt a legkisebb pontkülönbség
minPontKulonbseg = dontok[0]
for item in dontok:
    if item.pontkulonbseg() < minPontKulonbseg.pontkulonbseg():
        minPontKulonbseg = item
print(f"min pontkülönbség: {minPontKulonbseg.pontkulonbseg()}")
print("-----------------------------------------------")

#max
#Határozza meg a döntök során elért legnagyobb pont különbséget
maxPontKulonbseg = dontok[0]
for item in dontok:
    if item.pontKulonbseg() > maxPontKulonbseg.pontKulonbseg():
        maxPontKulonbseg = item
print(f"max pontkülönbség: {maxPontKulonbseg.pontKulonbseg()}")
print("-----------------------------------------------")

#Határozza meg hogy a döntök során milyen volt a maximális látogatottság

maxNezoszam= dontok[0]
for item in dontok:
    if item.maxNezoszam() > maxNezoszam.nezoszam():
        maxNezoszam = item
print(f"max Nezoszam: {maxNezoszam.nezoszam()}")
print("-----------------------------------------------")

#megszámlálás tétele
#Határozza meg hogy a döntök során hányszor nyert Pittsburgh Steelers
dbPS = 0
for item in dontok:
    if item.gyoztes == "Pittsburgh Steelers":
        dbPS += 1
print(f"A 'Pittsburgh Steelers' csapat {dbPS} győzött a döntők során")
print("---------------------------------------------------")

#Eldöntés tétele
#Legalább egy elem teljesítse a feltételt
#Határozza meg hogy volt-e olyan döntő ahol a két csapat közötti pontkülönbség meghaladta az 50-et

vanEpontKul50tobb = False
for item in dontok:
    if item.pontkulonbseg() > 50:
        vanEpontKul50tobb = True
        break
if vanEpontKul50tobb:
    print("Igen volt megfelelő döntő")
else:
    print("Nem volt megfelelő döntő")
print("-----------------------------------------------------")

#minden elem teljesíti
#Határozza meg hogy a döntők során minden egyes döntő a látogatottság meghaladta e a 70000-et

mindenEnezoszam70eTobb = True
for item in dontok:
    if not (item.nezoszam  > 70000):
        mindenEnezoszam70eTobb = False
        break
if mindenEnezoszam70eTobb:
    print ("Minden döntő teljesíti a feltételt")
else: 
    print ("Nem minden döntő teljesíti a feltételt")
print("----------------------------------------------------")


#kiválasztás tétele
#!!!!!!!!!!!!!!!!!!
#Határozza meg az első olyan döntőt  ahol a nézőszám meghaladta a 100000-et

dontoNezoszam100Etobb = None
for item in dontok:
    if item.nezoszam > 100000:
        dontoNezoszam100Etobb = item
        break
if dontoNezoszam100Etobb != None:
    print(f"Van ilyen döntő, amely nézőszáma: {dontoNezoszam100Etobb.nezosszam}")
else:
    print("Nincs megfelelő döntő")
print("--------------------------------------------------------------------")

#keresés tétele
#!!!!!!!!!!
#Keresse meg az első olyan dontőt amelyiknél a pontkülönbség a csapatok között 10
IndexPontKul10 = None
for i in range(len(dontok)):
    if dontok[i].pontkulonbseg() == 10:
        IndexPontKul10 = i
        break
if IndexPontKul10 != None:
    print(f"Döntő : {dontok[IndexPontKul10]}, NÉZŐSZÁM: {dontok[IndexPontKul10].nezoszam}")
else:
    print("Nincs megfelelő döntő")
print("----------------------------------------------------------")

#buborékos rendezés
#Rendezze a döntőket pontkülönbség alapján csökkenő sorrendben
for i in range(len(dontok)-1, 0, -1):
    for j in range(i):
        if dontok[j].pontkulonbseg() < dontok[j+1].pontkulonbseg():
            dontok[j], dontok[j+1] = dontok[j+1], dontok[j]

for item in dontok:
    print(item)
