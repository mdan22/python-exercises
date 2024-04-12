#Logische Operatoren

print("Willkommen in der Lotterie")

number1 = int(input("Bitte 1.Zahl eingeben: "))
number2 = int(input("Bitte 2.Zahl eingeben: "))
number3 = int(input("Bitte 3.Zahl eingeben: "))

if number1 == 3 and number2 == 14 and number3 == 22:
    print("Herzlichen Glückwunsch, du hast die Lotterie gewonnen!")
else:
    print("Du hast leider verloren ...")