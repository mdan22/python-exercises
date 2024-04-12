#while loops = a statement that will execute it's block of
#              code as long as it's condition remains true.

name = None

# or name = ""
# or while len(name) == 0:

while not name:
    name = input("Enter your name: ")

print("Hello "+name)