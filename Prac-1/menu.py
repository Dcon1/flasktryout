user_name = input("Please enter your name")
choice = input("(H)ello \n (G)oodbye \n (Q)uit")
while choice != "Q":
    if choice == "H":
        print("hello " +(user_name))
    elif choice == "G":
        print("goodbye " +(user_name))
    else:
        print("invalid choice")
    choice = input("(H)ello\n(G)oodbye\n(Q)uit")
print("Finshed")