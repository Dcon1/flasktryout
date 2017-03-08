"""
Author: Danny Connolly
"""
def main():
    user_name = get_name()
    for i in range(0, len(user_name) + 1, 2):
        print(user_name[i])


def get_name():
    name = input("Please enter your name")
    while name == "":
        name = input("Please enter your name")
    return name


main()