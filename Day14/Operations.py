
def main():
    print('Order of execution of Mathematical Operators in Python')
    print('PEMDAS')
    print('Parenthesis ()')
    print('Exponents **')
    print('Multiplication *')
    print('Division /')
    print('Addition +')
    print('Subtraction -')
    #
    # In Python, the order of execution of mathematical operations follows the usual rules of arithmetic, which is known as the "order of operations." The order of operations is typically remembered using the acronym PEMDAS, which stands for:
    #
    # Parentheses
    # Exponents (i.e., powers and square roots, etc.)
    # Multiplication and Division (left-to-right)
    # Addition and Subtraction (left-to-right)
    # So, when you have an expression like 3*3+3/3-3, here's how it's evaluated step by step:
    #
    # Multiplication: 3*3 equals 9.
    # Division: 3/3 equals 1.
    # Addition: 9 + 1 equals 10.
    # Subtraction: 10 - 3 equals 7.
    # So, the final result of the expression 3*3+3/3-3 is 7. The operations are performed from left to right following the order of operations, as described above.
    print(3*3+3/3-3)




if __name__ == '__main__':
    main()