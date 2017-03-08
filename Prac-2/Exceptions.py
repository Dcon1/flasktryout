numerator = int(input("Enter the numerator: "))
denominator = int(input("Enter the denominator: "))
fraction = numerator / denominator
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

#1.     When will a ValueError occur? When the integers are not valid numbers
#2.     When will a ZeroDivisionError occur? when one of the integers is a 0
#3.   Could you change the code to avoid the possibility of a ZeroDivisionError? an if statement checking the integer value of the number