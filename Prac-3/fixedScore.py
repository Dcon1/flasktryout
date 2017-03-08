def main():
    score = float(input("Enter score: "))
    final_result = get_result(score)
    print(final_result)


def get_result(score):
    if score < 0:
        return "Invalid score"
    elif score > 100:
        return "Invalid score"
    elif score > 50:
        return "Passable"
    elif score > 90:
        return "Excellent"
    else:
        return "Bad"


main()