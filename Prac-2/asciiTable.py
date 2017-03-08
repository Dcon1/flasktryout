# Get the ASCII number of a character
UPPER_NUMBER = 127
LOWER_NUMBER = 33
get_num = int(input("Please enter a number to convert"))
while int(get_num) < LOWER_NUMBER or int(get_num) > UPPER_NUMBER:
    get_num = int(input("You must enter a number between {}, and {}".format(LOWER_NUMBER, UPPER_NUMBER)))
print("{0}, {1:>5}".format(get_num, chr(get_num)))

# Get the character given by an ASCII number
get_char = str(input("Please enter a character to convert"))
print("{0}, {1:>6}".format(get_char, ord(get_char)))