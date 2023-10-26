from string import capwords
def main():

    country_name = "austria"
    print(country_name.capitalize())
    print(country_name.upper())

    book_name = "alice's adventures in wonderland"
    print(capwords(book_name))

    # Count the Number of Occurrences of a Substring in a String in Python
    paragraph = '''At three in the morning the chief Sussex detective, obeying the urgent call from Sergeant Wilson of 
       Birlstone, arrived from headquarters in a light dog-cart behind a breathless trotter. By the five-forty train in 
       the morning he had sent his message to Scotland Yard, and he was at the Birlstone station at twelve o'clock to 
       welcome us. White Mason was a quiet, comfortable-looking person in a loose tweed suit, with a clean-shaved, 
       ruddy face, a stoutish body, and powerful bandy legs adorned with gaiters, looking like a small farmer, 
       a retired gamekeeper, or anything upon earth except a very favourable specimen of the provincial criminal 
       officer.'''

    substring = 'Birlstone'

    print(f'The substring "{substring}" shows up {paragraph.count(substring)} times in the paragraph.')

    # You can actually break a string into a list of words or join a list of words in a string in Python.
    string = 'Holmes was certainly not a difficult man to live with'

    word_list = string.split()
    print(word_list)

    word_list = ['Holmes ', 'was ', 'certainly ', 'not ', 'a ', 'difficult ', 'man ', 'to ', 'live ', 'with']
    string = ''

    string = string.join(word_list)
    print(string)

if __name__ == '__main__':
    main()