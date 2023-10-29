
print_hello = lambda: print('Hello World! Anonymous or Lambda Function')

def checkeven(number):
    if number % 2 == 0:
        return True
    else:
        return False

def main():
    numbers = [1, 2, 5, 4, 7, 88, 12, 15, 55, 77, 95]
    even_numbers = filter(checkeven, numbers)
    print(list(even_numbers))
    print_hello()

    # Lambda functions are useful when you want to pass a function as an argument to another function call.
    even_numbers_lambda = filter(lambda number: True if number % 2 == 0 else False, numbers)

    print(f'even number using lambda is: {list(even_numbers_lambda)}')

if __name__ == '__main__':
    main()