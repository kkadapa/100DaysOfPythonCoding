def calculateTemperature():
    temperature_in_celsius = input('What is the temperature in celsius?')
    temperature_in_fahrenheit = (float(temperature_in_celsius) * 1.8)+32
    print(f'{temperature_in_celsius} degree celsius is equivalent to {temperature_in_fahrenheit} degree fahrenheit.')

def main():
    name = input('What is your name?')
    age = int(input(f'How old are you {name}?'))
    current_year = int(input(f'What year is this again?'))

    print(f'If my calculations are right, you were born in {current_year - age}')


    calculateTemperature()

if __name__ == '__main__':
    main()


