play = True

while play:
    f = 273.15
    t = "Möchtest du von Grad Celsius nach Kelvin oder von Kelvin nach Celsius umrechnen? \n1: Von Kelvin nach Celsius \n2: Von Celsius nach Kelvin \n"
    x = input(t)
    while x != "1" and x != "2":
        x = input(t)

    if x == "1":
        kel = int(input("Wie viel Grad Kelvin (Ohne \"°Kelvin\")\n"))
        if kel < 0:
            print("Der eigegebene Wert ist unter dem Physikalischem \"Nullpunkt\"")
            e1 = kel - f
            z = str(e1) + "°C"
            print(z)
        else:
            e1 = kel - f
            z = str(e1) + "°C"
            print(z)
    elif x == "2":
        cel = int(input("Wie viel Grad Celsius? (Ohne \"°C\")\n"))
        e2 = cel + f
        if e2 < 0:
            print("Der errechnete Wert liegt unter 0°K und somit unter dem Physikalischen \"Nullpunkt\"")
            y = str(e2) + "°K"
            print(y)
        else:
            y = str(e2) + "°K"
            print(y)
    nochmal = input("Ja für nochmal rechnen\n")
    if nochmal.lower() != "ja":
        play = False

print("Programm beendet, Fenster kann nun geschlossen werden!")
