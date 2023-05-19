# Trečia užduotis
#
# Sukurti programą, kuri saugotų duomenis apie darbuotojus Pickle faile bei atliktų su duomenimis įvairius veiksmus:

# Sukurti funkciją, kuri sukuria darbuotoją (vardas, amžius, darbo pozicija) ir jį grąžina
# Sukurti funkciją, kuri išsaugo darbuotojus į failą (pickle)
# Sukurti funkciją, kuri užkrauna darbuotojus iš failo ir juos grąžina (pickle)


# Panaudoti sukūrimo funkciją kelis kartus su kokiomis norite reikšmėmis
# Panaudoti išsaugojimą į failą funkciją
# Panaudoti užkrovimo iš failo funkciją
# Atspausdinkite užkrautus iš failo duomenis


import pickle

def ivedame_darbuotojus(vardas, amzius, pozicija):
    darbuotojas = {'vardas': vardas, 'amzius': amzius, 'pozicija': pozicija}
    return darbuotojas
vardas = 'Jonas'
amzius = 20
pozicija = 'programuotojas'

rezultatas = ivedame_darbuotojus(vardas, amzius, pozicija)
#print(rezultatas)

import pickle

def isaugo_darbuotojus(darbuotojas):
    with open('darbuotojai.pickle', 'wb') as f:
        pickle.dump(darbuotojas, f)

darbuotojas = {'vardas': 'Jonas', 'amzius': 20, 'pozicija': 'programuotojas'}
isaugo_darbuotojus(darbuotojas)


def uzkrauna_darbuotojus(darbuotojas):
    with open('darbuotojai.pickle', 'rb') as f:
        darbuotojas = pickle.load(f)
print(darbuotojas)


# Panaudoti sukūrimo funkciją kelis kartus su kokiomis norite reikšmėmis
# Panaudoti išsaugojimą į failą funkciją
# Panaudoti užkrovimo iš failo funkciją
# Atspausdinkite užkrautus iš failo duomenis

def ivedame_darbuotojus(vardas, amzius, pozicija):
    darbuotojas = {'vardas': vardas, 'amzius': amzius, 'pozicija': pozicija}
    return darbuotojas
vardas = 'Jonas', 'Petras', 'Antanas, Linas'
amzius = 20, 30, 40, 50
pozicija = 'programuotojas', 'testuotojas', 'isilauzelis', 'java programuotojas'

rezultatas = ivedame_darbuotojus(vardas, amzius, pozicija)
#print(rezultatas)


def isaugo_darbuotojus(darbuotojas):
    with open('darbuotojai.pickle', 'wb') as f:
        pickle.dump(darbuotojas, f)

darbuotojas = rezultatas
isaugo_darbuotojus(darbuotojas)


def uzkrauna_darbuotojus(darbuotojas):
    with open('darbuotojai.pickle', 'rb') as f:
        darbuotojas = pickle.load(f)
print(darbuotojas)









