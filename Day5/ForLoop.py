def main():
    random_numbers = [6, 1, 3, 8, 0, 9, 12, 3, 4, 0, 54, 8, 100, 55, 60, 70, 85]

    for number in random_numbers:
        print(number)

    multiplied_random_numbers = []

    #multiply it by 2 and print out the resultant value instead
    for no in random_numbers:
        multiplied_random_numbers.append(no*2)

    print(multiplied_random_numbers)

    number = 1
    while number < 11:
        print(number)
        number += 1

if __name__ == '__main__':
    main()