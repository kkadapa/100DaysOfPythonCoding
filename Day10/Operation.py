
def main():
    # Read the input as two integers separated by a space
    a, b = map(int, input().split())

    # Calculate the maximum value by considering all 4 operations
    max_value = max(a*b, a//b, a-b, a+b)

    # Print the maximum value
    print(max_value)

if __name__ == '__main__':
    main()