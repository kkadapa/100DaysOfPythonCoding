
def main():
    horror_books = ['Dracula', 'Carmilla', 'The Imago Sequence']
    print(horror_books)

    a_random_list = ['Dracula', 1, 5.7, 'Carmilla']
    print(a_random_list)

    #Lists in Python are mutable. This means you can modify a list after its creation. For example, you can use the pop() method to get rid of the last value in a list.

    print(horror_books.pop())
    print(horror_books)

    #append() method for inserting new item to the list.

    horror_books.append('The Exorcist')

    print(horror_books)

if __name__ == '__main__':
    main()