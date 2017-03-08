user_choice = int(input("Please choose what you would like to do between choice 1 - 4\n1. Show the even numbers.\n2. Show the odd numbers.\n3. Show the squares.\n4. Quit."))
while user_choice != 4:
    num_one = int(input("Thank you please enter the first number"))
    num_two = int(input("Now please enter the second number"))
    if user_choice == 1:
        for i in range(num_one, num_two, 2):
            print(i)
        print()
    elif user_choice == 2:
        for i in range(num_one, num_two, -1):
            print(i)
    elif user_choice == 3:
        for i in range (num_one, num_two, 10):
            print(i,)
    else:
        print("invalid choice")
    user_choice = int(input("Please choose what you would like to do between choice 1 - 4\n1. Show the even numbers.\n2. Show the odd numbers.\n3. Show the squares.\n4. Quit."))
print("Thank you for using the number sequence generator")