
def main():
    print('Welcome to Life In Weeks')

    age = int(input('Enter your current age'))

    if age < 90:
        years = 90 - age
        weeks = years * 52
        print(f'You have {weeks} weeks left')
    else:
        print('Please enter age less than 90 years')


if __name__ == '__main__':
    main()