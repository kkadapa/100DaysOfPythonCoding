
message = 'Hello, {name}!'

def main():
    global message

    message = message.format(name='Farhan')
    print(message)

    print('This is about How to Work with local, nonlocal and global Variables in Python.')

    # Scope of a variable in Python or programming in general refers to region where that variable is accessible.

    # This is where the global keyword comes in. Instead of creating a local variable, you can let Python know that
    # you're trying to access the global message variable.




if __name__ == '__main__':
    main()