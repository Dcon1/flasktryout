# Get the ASCII number of a character
UPPER_NUMBER = 127
LOWER_NUMBER = 33


def main():
    user_number = get_number(LOWER_NUMBER, UPPER_NUMBER)
    print(user_number)
    # Get the character given by an ASCII number
    get_char = str(input("Please enter a character to convert"))
    print("{0}, {1:>6}".format(get_char, ord(get_char)))


def get_number(lower, upper):
    get_num = 0
    while int(get_num) < lower or int(get_num) > upper:
        try:
            get_num = int(input("You must enter a number between {}, and {}".format(lower, upper)))
        except ValueError:
            print("Value error recieved, please select a valid integer")
        print("you must enter a vaild integer")
    number = ("{0}, {1:>5}".format(get_num, chr(get_num)))
    return number



main()
