def main():

    start = int(input('Which number do you want to start from?\n-'))
    end = int(input('Which number do you want to stop at?\n-'))

    total = 0

    for number in range(start, end+1):
        total += number

    print(f'The sum of the numbers between {start} and {end} is: {total}')


if __name__ == '__main__':
    main()