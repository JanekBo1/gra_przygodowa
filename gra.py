from plansze import *
from dialogi import *
from przedmioty import *
import os, sys
from save import *

plecak_bohatera = ["zwykly_miecz", "zwykly_lok"]
zycie = ["=", "="]
mana = ["=", "=", "=", "=", "=", "=", "=", ]


def pokaz_przedmioty(plecak_bohatera):
    for przedmiot in range(len(plecak_bohatera)):
        nazwa_przedmiotu = plecak_bohatera[przedmiot]     

        if nazwa_przedmiotu in przedmioty["bron"]:
            print(f"posiadasz: {plecak_bohatera[przedmiot]}")
            print(f"   typ: {przedmioty['bron'][nazwa_przedmiotu]['typ']} ")
            print(f"   atak: {przedmioty['bron'][nazwa_przedmiotu]['atak']} ")
            print(f"   obrona: {przedmioty['bron'][nazwa_przedmiotu]['obrona']} ")
            print("\n")

        else:
            print(f"posiadasz: {plecak_bohatera[przedmiot]}")
            print(f"   opis:  {przedmioty['artefakty'][nazwa_przedmiotu]['opis']}")


def plansza(zycie):
    print("życie:", end = "")
    for pasek_zycia in range(len(zycie)):
        print(zycie[pasek_zycia], end = "")

    print("     mana:", end = "")
    for pasek_mana in range(len(mana)):
        print(mana[pasek_mana], end = "")

    for i in range(len(mapa_1)):
        print("")
        for j in range(len(mapa_1[0])):
            print(mapa_1[i][j], end="")
    print("\n")




def walidacja_ruchu(x, y, mapa_1, zycie):
    if mapa_1[x][y] == " ":
        return "dozwolony", zycie

    elif x == 1 and y == 5:
        mapa_1, zycie = dialog_1(mapa_1, plecak_bohatera, zycie)
        return "dialog", zycie

    elif x == 28 and y == 15:
        dialog_2(plecak_bohatera)

    elif x == 28 and y == 2:
        plecak_bohatera.append("ksiega_czarow")
        return "dozwolony", zycie

    elif mapa_1[x][y] == "P":
        plecak_bohatera.append("zardzewialy_klucz")
        return "dozwolony", zycie

    else:
        print("ruch niedozwolony")
        return "niedozwolony", zycie


def dodanie_przedmiotu(mapa_1):
    mapa_1[28][2] = "P"
    mapa_1[28][15] = "N"
    return mapa_1

def save(mapa_1):
    with open(f"save.py", "w") as f:
        wiersz1 = f"zapis = {str(mapa_1)}"
        wiersz2 = f"zapisany_x = {x}"
        wiersz3 = f"zapisany_y = {y}"
        wiersz4 = f"zapisany_plecak_bohatera = {plecak_bohatera}"
        f.write(f"{wiersz1}\n{wiersz2}\n{wiersz3}\n{wiersz4}")

def load(zapis, zapisany_x, zapisany_y, zapisany_plecak_bohatera):
    mapa_1 = zapis
    x = zapisany_x
    y = zapisany_y
    plecak_bohatera = zapisany_plecak_bohatera
    return mapa_1, x, y, plecak_bohatera

#main

mapa_1 = dodanie_przedmiotu(mapa_1)

x = 1
y = 1
mapa_1[x][y] = "X"
plansza(zycie)
while True:

    ruch = input()
    if ruch == "w":
        walidacja, zycie = walidacja_ruchu(x-1, y, mapa_1, zycie)
        if walidacja == "dozwolony":
            mapa_1[x][y] = " "
            x = x - 1
            mapa_1[x][y] = "X"

    elif ruch == "s":
        walidacja, zycie = walidacja_ruchu(x+1, y, mapa_1, zycie)
        if walidacja == "dozwolony":
            mapa_1[x][y] = " "
            x = x + 1
            mapa_1[x][y] = "X"

    elif ruch == "a":
        walidacja, zycie = walidacja_ruchu(x, y-1, mapa_1, zycie)
        if walidacja == "dozwolony":
            mapa_1[x][y] = " "
            y = y - 1
            mapa_1[x][y] = "X"

    elif ruch == "d":
        walidacja, zycie = walidacja_ruchu(x, y+1, mapa_1, zycie)
        if walidacja == "dozwolony":
            mapa_1[x][y] = " "
            y = y + 1
            mapa_1[x][y] = "X"
    elif ruch == "i":
        pokaz_przedmioty(plecak_bohatera)

    elif ruch =="save":
        save(mapa_1)  
        print("mapa została zapisana") 

    elif ruch =="load":
        mapa_1, x, y, plecak_bohatera = load(zapis, zapisany_x, zapisany_y, zapisany_plecak_bohatera)   

    elif ruch =="exit":
        exit(0)

    else:
        print("poruszaj sie uzywajc klawiszy w s a d")
    plansza(zycie)