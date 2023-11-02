

def main():
    print('Welcome to BMI Calculator')

    weight = int(input('Please enter your weight\n'))

    height = float(input('Please enter your height\n'))

    BMI = weight / (height*height)
    bmi_as_int = int(BMI)
    print(f'Your BMI is {bmi_as_int}')


if __name__ == '__main__':
    main()