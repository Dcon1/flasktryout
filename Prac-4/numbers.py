def main():
    numbers = []
    for i in range(0, 5, 1):
        user_num = int(input("Please enter 5 numbers, enter number {}".format(i + 1)))
        numbers.append(user_num)
    print("the first number is {}".format(numbers[0]))
    print("the last number is {}".format(5))
    print("The smallest number is {}".format(min(numbers)))
    print("The largest number is {}".format(max(numbers)))
    print("The average of numbers is {}".format((sum(numbers)/(len(numbers)))))


main()