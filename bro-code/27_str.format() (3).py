
# str.format() =    optional method that gives users
#                   more control when displaying output

#number = 3.14159
number = 1000

print("The number pi is {:.3f}.".format(number))
print("The number is {:,}.".format(number))
print("The number is {:b}.".format(number))
print("The number is {:o}.".format(number))  #octal number
print("The number is {:X}".format(number))  #hexadecimal number
print("The number is {:E}.".format(number)) #scientific notation