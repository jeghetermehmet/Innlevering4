steder = []
for i in range(5):
    steder.append(input("Skriv et reisemål: "))
klesplagg = []
avreisedatoer = []
for i in range(5):
    klesplagg.append(input("Skriv et klesplagg: "))
for i in range(5):
    avreisedatoer.append(input("Skriv et avreisedato: "))
reiseplan = []
reiseplan.append(steder)
reiseplan.append(klesplagg)
reiseplan.append(avreisedatoer)
for i in reiseplan:
    print(i) #det skrives ut tre lister med sine innhold.

liste_indeks1 = int(input("Skriv et nummer 0,1 eller 2. Der tilsvarer 0 steder, 1 er klesplagg, 2 er avreisedatoer"))
liste_indeks2 = int(input("Skriv et nummer 0,1,2,3,eller 4 for elementene i listen du vil ha"))

if (liste_indeks1 >= 0 and liste_indeks1 <= 2) and (liste_indeks2 >= 0 and liste_indeks2 <= 4):
    print(reiseplan[liste_indeks1][liste_indeks2])
else:
    print("Ugyldig input!")



