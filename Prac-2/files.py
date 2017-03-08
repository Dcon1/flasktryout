name = input("Please enter your name")
file = open('data.txt', mode='w')
file.write(name)
file.close()

open_file = open("data.txt", mode= "r")
first_line = open_file.readline()
print("your name is ", first_line)
open_file.close()