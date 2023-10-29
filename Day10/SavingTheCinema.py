def main():
    movie_char = {
        'Yoda': 'Pertenece a Star Wars.',
        'Spock': 'Pertenece a Star Trek.',
        'Frodo': 'No pertenece ni a Star Wars ni a Star Trek.'
    }

    userinput = input('')
    print(movie_char.get(userinput))

if __name__ == '__main__':
    main()
