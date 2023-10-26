def main():
    number = int(input('what number would you like to check?\n- '))

    if number % 2 == 0:
        print(f'{number} is even.')
    else:
        print(f'{number} is odd.')

# Check whether a year is leap year or not
    year = int(input('which year would you like to check?\n- '))

    if year % 400 == 0 and year % 100 == 0:
        print(f"{year} is leap year.")
    elif year % 4 == 0 and year % 100 != 0:
        print(f"{year} is leap year.")
    else:
        print(f"{year} is not leap year.")

# Check whether a number is prime or not
    pnumber = int(input('what number would you like to check?\n- '))

    is_not_prime = False

    if pnumber == 1:
        print(f"{pnumber} is not a prime number")
    elif pnumber > 1:
        for n in range(2, pnumber):
            if(pnumber % n) == 0:
                is_not_prime = True
                break

        if is_not_prime:
            print(f"{pnumber} is not a prime number.")
        else:
            print(f"{pnumber} is a prime number.")


if __name__ == '__main__':
    main()
