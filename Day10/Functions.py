def main():
    print(hello('Hello, Universe!'))
    print(hello('Hello, Universe!', True))

    # make a function accept multiple arguments and even set a default value for it.

def hello(message, is_lower=False):
    if is_lower:
        return message.lower()
    else:
        return message.upper()


        x = 3
        y = 4
        z = 5
        print(x if not x+y*z else y)

if __name__ == '__main__':
    main()
