import random
MIN_NUM = 1
MAX_NUM = 45


def main():
    game_lines = int(input("How many quick picks"))
    for i in range(0, game_lines, 1):
        game_numbers = []
        for i in range(0, 6, 1):
            random_number = random.randint(MIN_NUM, MAX_NUM)
            while random_number in game_numbers:
                random_number = random.randint(MIN_NUM, MAX_NUM)
            game_numbers.append(random_number)
        print("{}".format(sorted(game_numbers)))


main()
