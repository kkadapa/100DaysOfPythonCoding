def main():
    print('Welcome to Band name generator!')

    city_name = input('Which city did you grew up in?\n')

    pet_name = input("What's the name of your pet?\n")

    band_name = city_name + pet_name
    print(f'Your Band name is {band_name} \n')



if __name__ == '__main__':
    main()