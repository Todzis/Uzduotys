# Ketvirta užduotis
#
# Sukurti funkciją, kuri priimtų sąrašą tuple elementų, kiekvienas tuple sudarytas iš 2 elementų - stringo ir
# sąrašo
# int
# skaičių. Funkcija turi grąžinti sąrašą tuple elementų, kurie sudaryti iš 2 reikšmių: stringo ir skaičių vidurkio:
# Pvz: į funkciją paduodamas sąrašas: [c), ("banana", [4, 5, 6]), ("orange", [7, 8, 9])], turi būti grąžinamas: [("apple", 2.0), ("banana", 5.0), ("orange", 8.0)]

# Panaudoti sukurtą funkciją su kokiomis norite reikšmėmis ir atspausdinti funkcijos rezultatus


#



def sukurti_tuple():
    zodynas = {'pavadinimas': [], 'vidurkiai': []}

    while True:
        preke = input("Įveskite prekės pavadinima arba įrasykite 'exit' norėdami iseiti: ")
        if preke.lower() == "exit":
            break

        skaiciai = []
        while True:
            skaicius = input("Įveskite skaiciu arba įrasykite 'done' jei norite baigti: ")
            if skaicius.lower() == "done":
                break
            skaiciai.append(int(skaicius))
        vidurkis = sum(skaiciai) / len(skaiciai)

        zodynas['pavadinimas'].append((preke, skaiciai))
        zodynas['vidurkiai'].append(vidurkis)

    return zodynas

rezultatas = sukurti_tuple()
print(rezultatas)

for i in range(len(rezultatas['pavadinimas'])):
    print(rezultatas['pavadinimas'][i], rezultatas['vidurkiai'][i])










