def dialog_1(mapa_1, plecak_bohatera, zycie):
    print("daj mi klucz")
    if "zardzewialy_klucz" in plecak_bohatera:
        print("dzięki")
        zycie = zycie[:-1]
        plecak_bohatera.remove("zardzewialy_klucz")
        mapa_1[5][5] = " "
        return mapa_1, zycie
    else:
        print("niemasz klucza")


def dialog_2(plecak_bohatera):
    if "ksiega_czarow" in plecak_bohatera:
        print("widzę, że znalazłeś księge super")
    else:
        print("jeśli szukasz czegoś cennego to w tamtym pokoju jest księga, możesz ją sobie wziąść")

def dialog_3()
print("1")