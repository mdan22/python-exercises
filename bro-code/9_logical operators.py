# logical operators (and,or,not) = used to check if two ore more conditional statements are true.

temp = int(input("What is the temperature outside?: "))

if temp >= 0 and temp <= 30:
    print("The temperature is good today!")
    print("Go outside!")
elif temp < 0 or temp > 30:
    print("The temperature is bad today!")
    print("Stay inside!")

# not(conditional statements) # flips true to false or false to true