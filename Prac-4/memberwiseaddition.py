"""
I could not figure out how to add diferent size lists together with out getting an index range error
Again I needed to add in an if statement on line 15,I feel there is a better way to do this but cant work it out.
if I put in the following on line 14 -
for len in first_numbers
is it the same as the for loop I used?
"""


def main():
    first_numbers = [1, 2, 3, 7]
    second_numbers = [2, 3, 4, 5]
    combined_numbers = []
    for i in range(0, len(first_numbers), 1):
        if len(combined_numbers) < 0:
            combined_numbers = first_numbers[i] + second_numbers[i]
        else:
            combined_numbers.append(first_numbers[i] + second_numbers[i])
    print(combined_numbers)


main()
