from random import *
import time

zycie_gracza = ["=", "=", "=", "=", "=", "="]
mana_gracza = ["=", "=", "=", "=", "=", "=", "="]
zycie_przeciwnika = ["=", "=", "=", "="]

def wyswietl_informacje(zycie_gracza, zycie_przeciwnika, mana_gracza, tura):
    print(f"XXXXXXXXXXXXXXX POZOSTALO {len(mana_gracza) - tura} TUR DO KONCA XXXXXXXXXXXXXXX")
    print("życie gracza:", end = "")
    for pasek_zycia in range(len(zycie_gracza)):
        print(zycie_gracza[pasek_zycia], end = "")
    print("\n")
    print("życie przeciwnika:", end = "")
    for pasek_zycia in range(len(zycie_przeciwnika)):
        print(zycie_przeciwnika[pasek_zycia], end = "")
    print("\n")
    print("wybierz akcje:")
    print("a -> atak")
    print("d -> dokladny atak")
    print("o -> obrona")
    print("l -> leczenie")




def walka(zycie_gracza, mana_gracza, zycie_przeciwnika):
    for tura in range(len(mana_gracza)):
        #TURA GRACZA
        wyswietl_informacje(zycie_gracza, zycie_przeciwnika, mana_gracza, tura)
        akcja_gracza = input("podaj litere odpowiadajaca nazwie akcji: ")
        if akcja_gracza == "a":
            zadane_obrazenia = randint(0, 2)
            zycie_przeciwnika = zycie_przeciwnika[:-zadane_obrazenia]
            print(f"zadales_przeciwnikowi {zadane_obrazenia} obrazen")
        elif akcja_gracza == "d":
            zycie_przeciwnika = zycie_przeciwnika[:-1]
            print(f"zadales_przeciwnikowi 1 obrazen")
        elif akcja_gracza == "l":
            zycie_gracza.append("=")
            print("wyleczyles sie o 1 punkt zycia")

        time.sleep(3)
        #TURA PRZECIWNIKA
        akcja_przeciwnika = randint(0, 1)

        if akcja_przeciwnika == 0:
            print("PRZECIWNIK ATAKUJE")
            zycie_gracza = zycie_gracza[:-randint(0, 2)]
        elif akcja_przeciwnika == 1:
            print("PRZECIWNIK SIE LECZY")
            zycie_przeciwnika.append("=")


        print("\n")



#main

walka(zycie_gracza, mana_gracza, zycie_przeciwnika)