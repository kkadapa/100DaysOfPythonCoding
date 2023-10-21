from library import greet

def main():
    greet()

    #Declare variables like below

    book = 'Dracula'
    author = 'Bram Stoker'
    release_year = 1897
    goodreads_rating = 4.01

    print(book)
    print(author)
    print(release_year)
    print(goodreads_rating)

    #or declare variables like below and print in one go

    book, author, release_year, goodreads_rating = 'Dracula', 'Bram Stoker', 1897, 4.01

    # print(book, author, release_year, goodreads_rating)

    print(book + ' is a novel by' + author + ', published in ' + str(release_year) + '. It has a rating of ' + str(goodreads_rating) + ' on goodreads.')

if __name__ == '__main__':
    main()


