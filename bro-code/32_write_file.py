text = "Yooo\nThis is some text\nHave a good one!\n"
with open('test.txt','w') as file: #write to a file
    file.write(text)

text = "Have a nice day! See ya"
with open('test.txt','a') as file: #append a file
    file.write(text)