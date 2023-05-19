# Penkta užduotis
#
# Sukurti programą, kuri nuskaitys iš .txt failo skaičius
# (failą kokį norite susikurkite bei užpildykite kokiais norite skaičiais),
# suskaičiuos visų skaičių vidurkį (naudojant reduce() funkciją)
# bei išsaugos rezultatą į kitą .txt  failą (šį failą taip pat susikurkite kokį norite).
# Taip pat, tą patį vidurkį išspausdinkit ir į terminalą.

skaiciai = [1,2,3,4,5,6,7,8,9,10]

failo_pavadinimas = 'skaiciai.txt'

with open(failo_pavadinimas, 'w') as f:
    for skaicius in skaiciai:
        f.write(str(skaicius) + '\n')


failo_pavadinimas = 'skaiciai.txt'

with open(failo_pavadinimas, 'r') as f:
    sum = sum(skaiciai)
    vidurkis = sum / len(skaiciai)
    print(vidurkis)
