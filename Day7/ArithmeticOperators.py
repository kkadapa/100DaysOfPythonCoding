def main():
    books = ['Dracula', 'Frankenstein', 'The Omen', 'The Exorcist', 'The Legend of Sleepy Hollow']
    more_books = ['And Then There Were None', 'The ABC Murders', 'The Valley of Fear', 'The Hound of the Baskervilles',
                  'The Chestnut Man']

    print(f'Addition',books+more_books,'\n')

    # The * operator, on the other hand, makes multiple copies of a given sequence.
    print(f'Multiplication',books * 2,'\n')

    # The len() function can return the length of a given sequence
    # The min() and max() functions can return the minimum and maximum value in a given sequence
    random_numbers = [6, 1, 3, 8, 0]

    print(f'Length Function',len(random_numbers),'\n')
    print(f'Min Function',min(random_numbers),'\n')
    print(f'Max Function',max(random_numbers))




if __name__ == '__main__':
    main()