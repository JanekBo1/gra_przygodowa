#!/bin/env python3
import datetime, os, sys

def ile_dni_zyjesz(rok, miesiac, dzien, dzisiaj):
    rok = int(rok)
    miesiac = int(miesiac)
    dzien = int(dzien)
    dzien_urodzin = datetime.datetime(rok, miesiac, dzien)
    ilosc_dni = dzisiaj - dzien_urodzin
    return ilosc_dni

#main
dzisiaj = datetime.datetime.now()

while True:
    rok = input("podaj rok swoich urodzin: ")
    if rok.isnumeric() is True:
        break
    print("rok musi byc podany w postaci liczby")

miesiac = input("podaj miesiac swoich urodzin: ")
dzien = input("podaj dzien swoich urodzin: ")
ilosc_dni = ile_dni_zyjesz(rok, miesiac, dzien, dzisiaj)

print(f"na tym swiecie zyjesz juz {ilosc_dni}")
with open(f"zapisane urodziny.txt", "w") as f:
    f.write(f"na tym swiecie zyjesz juz {ilosc_dni}")