def main():
    a_range = range(10)
    print(a_range)

    list_a_range = list(a_range)
    print(list_a_range)

    #The most basic usage of a index is to access its corresponding value from the sequence.
    horror_books = ['Dracula', 'Carmilla', 'The Imago Sequence']

    print(horror_books[0])
    print(horror_books[1])
    print(horror_books[2])

    # You can also use negative numbers as indices but in that case the counting will start from the end.
    books = ['Dracula', 'Frankenstein', 'The Omen', 'The Exorcist', 'The Legend of Sleepy Hollow',
             'And Then There Were None', 'The ABC Murders', 'The Valley of Fear']

    print(books[0])

    print(books[1])
    print(books[-1])

    print(books[2])
    print(books[-2])

if __name__ == '__main__':
    main()