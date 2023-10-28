
def main():
    numbers_list = set([1, 2, 3, 4, 5, 3, 2, 4])

    for num in numbers_list:
        print(f'num is {num}')

    # Sets are mutable, so you can add new values to a set using the add() method.
    numbers_list.add(450)
    print(f'mutable adding 500 {numbers_list}')

    # discard() method to remove an item from a set
    numbers_list.discard(3)
    print(f'discard test {numbers_list}')

    # clear() method to remove all values altogether.
    numbers_list.clear()
    print(f'clear removes all values {numbers_list}')

if __name__ == '__main__':
    main()