

def main():
    print('Welcome to Roller Coaster!')

    height = int(input('Please enter your height\n'))

    if height >= 120:
        age = int(input('Please enter your age\n'))
        if age > 18:
            print('$12')
        elif age < 12:
            print('$5')
        elif 12 < age < 18:
            print('$7')
    else:
        print("Sorry you are not eligible to ride now")



if __name__ == '__main__':
    main()