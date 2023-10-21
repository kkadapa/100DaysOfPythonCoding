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

    num_1 = 15
    num_2 = 12

    print(f'sum of num_1 and num_2 is: {num_1 + num_2}')
    print(f'difference of num_1 and num_2 is: {num_1 - num_2}')
    print(f'difference of num_2 and num_1 is: {num_2 - num_1}')
    print(f'product of num_1 and num_2 is: {num_1 * num_2}')
    print(f'quotient of num_1 and num_2 is: {num_1 / num_2}')
    print(f'floored quotient of num_1 and num_2 is: {num_1 // num_2}')

    float_variable = 1.25
    integer_variable = 55

    print(f'{float_variable} converted to an integer is : {int(float_variable)}')
    print(f'{integer_variable} converted to a float is: {float(integer_variable)}')

    #How to take inputs from users in python

    name = input('What is your name?')

    print(f'Nice to meet you {name}')

if __name__ == '__main__':
    main()


