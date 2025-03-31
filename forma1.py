"""
Olvasd be az f1.txt adatait, majd oldd meg az alábbi feladatokat!

1. Hány versenyző szerepel a fájlban?
2. Melyik versenyző nyerte a legtöbb futamot?
3. Ki teljesített a legtöbb futamot?
4. Átlagosan hány futamot teljesítettek a versenyzők?"

A megoldott feladatokat a kiirt_adatok nevű mappába hozd létre statisztika.txt néven!
"""
"""versenyzok_szama = 0
with open('beolvasando_adatok/f1.txt', 'r', encoding="utf-8") as forras_falj: 
    for sor in forras_falj:
        versenyzok_szama += 1

legtobb_nyeres = []
for sor in forras_falj:
    adatok = sor.split(',')
    if adatok[2] > legtobb_nyeres:
        legtobb_nyeres.append(adatok[2])
print(legtobb_nyeres)"""


adatok = []
gyozelmeke = []
futamoke = []
atlag_a = 0
with open('beolvasando_adatok/f1.txt', 'r', encoding='utf-8') as forrasfajl:
    next(forrasfajl)
    for sor in forrasfajl:
        adat = sor.strip().split(';')
        nev = adat[0]
        csapat= adat[1]
        gyozelmek = int(adat[2])
        futamok = int(adat[3])
        atlag_a = atlag_a + futamok
        adatok.append(nev)
        gyozelmeke.append(gyozelmek)
        futamoke.append(futamok)
    legtobb_gyozelem = max(gyozelmeke)
    legtobb_gyozelem_indexe = gyozelmeke.index(legtobb_gyozelem)
    legtobb_futam = max(futamoke)
    legtobb_futam_indexe = futamoke.index(legtobb_futam)
    atlag = atlag_a / len(adatok)
    atlag = float(atlag)
    
    


print(f"A beolvasott fájlban összesen {len(adatok)} versenyző szerepel.")
print(f"A legtöbb futamot nyert versenyző: {adatok[legtobb_gyozelem_indexe], legtobb_gyozelem} ")
print(f"A legtöbb futamot teljesített versenyző: {adatok[legtobb_futam_indexe]} ")
print(f"Az átlagos futamszám: {atlag} ")

