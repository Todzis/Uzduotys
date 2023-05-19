
#Per visa skirta laika padariau tik 3 uzduotis, ir benra uzduoti uplaudinau per gita.


# likusias uzduotis padariau del praktikos nes vis dar labai ilgai uztruka rasyt viena
# ar kita kodo eilute.

# Prisegu visas




# Pirma užduotis
#
# Sukurti funkciją, kuri iš vardų sąrašo sudarytų sąrašą tik iš vardų pirmų raidžių ir tą sąrašą grąžintų:
# Pvz: paduodamas sąrašas į funkciją: [‘Jonas’, ‘Petras’, ‘Linas’], tai grąžinamas turėtų būti [‘J’, ‘P’, ‘L’]
# Paduoti vardų sąrašą į funkciją (vardus galite sugalvoti patys) ir atspausdinti funkcijos rezultatą

sarasas = ['Jonas', 'Petras', 'Linas']


def gauti_pirmasraides(sarasas):
    pirmos_raides = []
    for raide in sarasas:
        pirmos_raides.append(raide[0])
    return pirmos_raides

pirmos_raides = gauti_pirmasraides(sarasas)
print(pirmos_raides)