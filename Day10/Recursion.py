
# Without recursion
def natural_sum(last_number):
    if last_number < 1:
        return last_number

    total = 0
    for number in range(1, last_number+1):
        total += number

    return total

# with recursion
def recursive_natural_sum(last_number):
    if last_number < 1:
        return last_number

    return last_number + recursive_natural_sum(last_number - 1)

def main():
    last_number = int(input('Up to which number would you like to calculate the sum'))
    print(natural_sum(last_number))
    print(recursive_natural_sum(last_number))

if __name__ == '__main__':
    main()