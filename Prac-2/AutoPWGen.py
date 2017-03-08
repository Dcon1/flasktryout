import random
LETTERS = "aeioubcdfghjklmnpqrstvwxyz"
NUMBERS = "1234567890"
MIN_LENGTH = 2
MAX_LENGTH = 8
SPECIAL_CHARS_REQUIRED = "TRUE"
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]\<>?{}| "

def main():


    upper_char = int(input("How many upper case characters do you require between 0 and 9"))
    lower_char = int(input("How many lower case characters do you require between 0 and 9"))
    numeric_char = int(input("How many numbers do you require between 0 and 9"))
    special_char = int(input("How many special characters do you require between 0 and 9"))
    password = ""
    for i in range(0,upper_char,1):
        password += random.choice(LETTERS.upper())
    for i in range(0, lower_char,1):
        password += random.choice(LETTERS.lower())
    for i in range(0,numeric_char,1):
        password += random.choice(NUMBERS)
    for i in range(0,special_char,1):
        password += random.choice(SPECIAL_CHARACTERS)
    password = list(password)
    random.shuffle(password)
    password = "".join(password)
    print("Your password is: "+(str(password)))
    validate_password = password_validate(password)
    if validate_password == False:
        print("password is not valid")
    elif validate_password == True:
            print("password is valid")


def password_validate(password):
        if len(password) < MIN_LENGTH or len(password) > MAX_LENGTH:
            return False

        count_lower = 0
        count_upper = 0
        count_digit = 0
        count_special = 0
        for char in password:
            if char.islower():
                count_lower += 1
            elif char.isupper():
                count_upper += 1
            elif char.isnumeric():
                count_digit += 1
            else:
                count_special += 1
        if count_lower == 0 or count_upper == 0 or count_digit == 0:
            return False
        elif SPECIAL_CHARS_REQUIRED == "TRUE" and count_special == 0:
            return False
        else:
            return True


main()