import random

def main():
    print('Welcome to Random Module!')

    random_float = random.random()

    print(f'print float {random_float}')

    love_score = random.randint(1, 100)

    print(f'Your love score is {love_score}')


if __name__ == '__main__':
    main()