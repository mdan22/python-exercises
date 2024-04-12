#Funktionen
#Funktionalität des Programms wird in unterschiedliche Funktionen ausgelagert
#Funktion = Unterprogramm
#alt:
print("Das ist eine Ausgabe")#builtinfunction
variable = 1
print(type(variable))
#neu:
def say_hello():
    print("Hallo Daniel")
    print("Willkommen zurück")

say_hello()
print("Test")