
def main():
    print('For loops with Lists')


fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + "Pie")

#Range
total = 0
for number in range(1, 101):
    total += number
    print(number)


if __name__ == '__main__':
    main()