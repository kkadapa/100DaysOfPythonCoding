
def main():
    print('Welcome to BMI 2.0')

    height = float(input('Enter your height\n'))

    weight = int(input('Enter your weight\n'))

    BMI = int(weight / (height*height))

    if BMI < 18.5:
        print(f'Your BMI is {BMI}, you are underweight')
    elif BMI < 25:
        print(f'Your BMI is {BMI}, you have normal weight')
    elif BMI < 30:
        print(f'Your BMI is {BMI}, you are slightly overweight')
    elif BMI < 35:
        print(f'Your BMI is {BMI}, you are obese')
    else:
        print('You are clinically obese')

if __name__ == '__main__':
    main()