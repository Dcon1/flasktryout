#file = open("numbers.txt", mode="r")
#line_one = int(file.readline())
#line_two = int(file.readline())
#print(line_one + line_two)
#file.close()


file = open("numbers.txt", mode="r")
total = 0
for line in file:
    number = int(line)
    total += number
print(total)
file.close()