def main():
    shield = int(input('What is your shield level?'))
    sword = int(input('What is your sword level?'))

    # and condition

    if shield >= 45 and sword >= 48:
        print('You shall pass!')
    else:
        print('You shall not pass!')

    # or condition

    age = 10_000
    is_legally_dead = True

    if is_legally_dead or age > 500_000:
        print('you shall pass!')
    else:
        print('You shall not pass!')

    # not operator

    age = 800_000
    is_van_helsing = True

    if age > 500_000 and not is_van_helsing:
        print('You shall pass!')
    else:
        print('You shall not pass!')

if __name__ == '__main__':
    main()


