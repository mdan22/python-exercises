# tuple =   collection which is ordered and unchangeable
#           used to group together related data

student = ("Daniel",19,"male")

print(student.count("Daniel"))
print(student.index("male"))

for x in student:
    print(x)
    
if "Daniel" in student:
    print("Daniel is here!")