import random

def main():
    print('Welcome to Heads or Tails!')

    outcome = random.randint(0, 1)

    if outcome == 1:
        print('Heads')
    else:
        print('Tails')

if __name__ == '__main__':
    main()