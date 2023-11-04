
def main():
    print('Welcome to Odd or Even!')

    number = int(input('Enter your number!\n'))

    if number % 2 == 0:
        print('Even number')
    else:
        print('Odd number')


if __name__ == '__main__':
    main()