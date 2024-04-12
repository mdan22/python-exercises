
# str.format() =    optional method that gives users
#                   more control when displaying output

name = "Daniel"

print("Hello, my name is {}.".format(name))
print("Hello, my name is {:10}. Nice to meet you.".format(name))
print("Hello, my name is {0:10}. Nice to meet you.".format(name))
print("Hello, my name is {:<10}. Nice to meet you.".format(name))
print("Hello, my name is {:>10}. Nice to meet you.".format(name))
print("Hello, my name is {:^10}. Nice to meet you.".format(name))