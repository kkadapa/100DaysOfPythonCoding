def main():
    print('Add Even Numbers')

    target = int(input('Enter a number between 0 & 1000\n'))

    even_sum = 0

    for number in range(2, target+1, 2):
        even_sum += number

    print(f'total sum', even_sum)

if __name__ == '__main__':
    main()
