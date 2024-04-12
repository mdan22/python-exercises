#Funktionen mit Rückgabewert

def maximum(a, b):
    if a < b:
        return b
    else:
        return a

result = maximum(15, 10)
print(result)