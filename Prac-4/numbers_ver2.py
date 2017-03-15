def main():
    user_num = int(input("Please enter a number"))
    numbers = [user_num]
    while user_num >= 0:
        user_num = int(input("Please enter a number"))
        if user_num < 0:
            break
        numbers.append(user_num)
    for i in range(0,len(numbers),1):
        print("Number {}:{}".format(i + 1, numbers[i]))
    print("the first number is {}".format(numbers[0]))
    print("the last number is {}".format(5))
    print("The smallest number is {}".format(min(numbers)))
    print("The largest number is {}".format(max(numbers)))
    print("The average of numbers is {}".format((sum(numbers)/(len(numbers)))))


main()