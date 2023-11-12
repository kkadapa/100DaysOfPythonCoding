import random
import string

print('Welcome to the PyPassword Generator!')

letters = int(input('How many letters would you like in your password?\n'))

symbols = int(input('How many symbols would you like in your password?\n'))

numbers = int(input('How many numbers would you like in your password?\n'))


def generate_random_string(length=letters):
    # Combine lowercase letters and digits to create a pool of characters
    characters = string.ascii_lowercase + string.digits

    # Generate a random string of the specified length
    random_string = ''.join(random.choice(characters) for _ in range(length))

    return random_string

def generate_random_symbols(length=symbols):
    # Use string.punctuation to include all ASCII punctuation characters
    symbols = string.punctuation

    # Generate a random string of symbols of the specified length
    random_symbols = ''.join(random.choice(symbols) for _ in range(length))

    return random_symbols

def generate_random_numbers(length=numbers):
    # Use string.digits to include all digits (0-9)
    numbers = string.digits

    # Generate a random string of numbers of the specified length
    random_numbers = ''.join(random.choice(numbers) for _ in range(length))

    return random_numbers

random_symbols_string = generate_random_symbols()
random_string = generate_random_string()
random_numbers_string = generate_random_numbers()

final_string = random_string + random_symbols_string + random_numbers_string

print(final_string)

