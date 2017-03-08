finished = False
result = 0
while not finished:
    try:
        user_num = int(input("Please enter a number"))
        print("Your number is", user_num)
        pass
    except ValueError:
        print("Not a valid number")
print("Valid result is:", result)
