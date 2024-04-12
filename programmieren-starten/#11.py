#Die if-Anweisung mit elif- und else-Zweigen

age = int(input("Bitte gebe dein Alter ein: "))

if age < 18:
    print("Achtung, der Nutzer ist jünger als 18")
elif age == 18:#else if
    print("Der Nutzer ist exakt 18")
elif age == 19:
    print("Der Nutzer ist exakt 19")
else:
    print("Der Nutzer ist volljährig")

print("Programmende")