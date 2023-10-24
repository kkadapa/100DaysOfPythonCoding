def main():

    # The in operator is the most common way of checking for any object's existence.
    a_string = 'Little Red Riding-Hood comes to me one Christmas Eve to give me information of the cruelty and ' \
               'treachery of that dissembling Wolf who ate her grandmother. '

    print('Red' in a_string)

    # The in operator is not exclusive to strings. You can actually use it on any other collection type such as lists, tuples, and ranges.

    books = ['Dracula', 'Frankenstein', 'The Omen', 'The Exorcist', 'The Legend of Sleepy Hollow']
    movies = ('A Christmas Carol', 'The Sea Beast', 'Enchanted', 'Pinocchio', 'The Addams Family')
    numbers = range(10)

    print('A Christmas Carol' in books)
    print('Enchanted' in movies)
    print(5 in numbers)

    # You may also want to find out about the absence of an object using NOT object

    print('A Christmas Carol' not in books)
    print('Enchanted' not in movies)
    print(15 not in numbers)

if __name__ == '__main__':
    main()