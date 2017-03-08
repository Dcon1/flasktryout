"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""
__author__ = 'Lindsay Ward'
MENU = "C - Convert Celsius to Fahrenheit\nF - Convert Fahrenheit to Celsius\nQ (for quit)"


def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            fahernheit = get_fahernhiet()
            print("Result: {:.2f} F".format(fahernheit))
        elif choice == "F":
            celsius = get_celsius()
            print("Result: {:.2f} C".format(celsius))
        else:
            print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")

def get_fahernhiet():
    global celsius, fahrenheit
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit

def get_celsius():
    global fahrenheit, celsius
    fahrenheit = float(input("Fahrenheit: "))
    celsius = fahrenheit * 5 / 9 - 32
    return celsius

main()