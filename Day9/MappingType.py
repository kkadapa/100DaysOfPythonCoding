
def main():
    programming_books = {
        'C Programming Language': 35,
        'Introduction to Algorithms': 100,
        'Clean Code: A Handbook of Agile Software Craftsmanship': 50
    }

    print(f'{programming_books}\n')

    cpl = 'C Programming Language'
    algo = 'Introduction to Algorithms'

    print(f'The price of {cpl} is ${programming_books.get(cpl)} ')
    print(f'The price of {algo} is ${programming_books.get(algo)}')

    # Dictionaries are mutable, use square braces to access a dictionary item.
    key = 'C Programming Language'
    programming_books[key] = 45
    programming_books['The Pragmatic Programmer'] = 32

    print(f'{programming_books}\n')

    # Print all keys
    for key in programming_books.keys():
        print(f'All keys: {key}')

    # Print all Values
    for value in programming_books.values():
        print(f'All values: {value}')

    #  if you want both the keys and the values as tuples, you can use the items method.
    for item in programming_books.items():
        print(f'Items are: {item}')

if __name__ == '__main__':
    main()