
def main():
    print('Welcome to Roller Coaster!')

    height = int(input('Please enter your height\n'))
    rc_price = 0

    if height >= 120:
        age = int(input('Please enter your age\n'))
        if age > 18:
            print('$12')
            rc_price = 12
        elif age < 12:
            print('$5')
            rc_price = 5
        elif 12 < age < 18:
            print('$7')
            rc_price = 7

        wants_photo = input('Do you want a photo taken? Y or N.')
        if wants_photo == "Y":
            rc_price += 3

        print(f'Your final bill is {rc_price}')

    else:
        print("Sorry you are not eligible to ride now")


if __name__ == '__main__':
    main()