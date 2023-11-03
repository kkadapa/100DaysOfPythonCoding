
def main():
    print('Welcome to the roller coaster!')

    height = int(input('What is your height in cm?'))

    if height > 120:
        print('You can ride')
    else:
        print('You cannot ride')


if __name__ == '__main__':
    main()