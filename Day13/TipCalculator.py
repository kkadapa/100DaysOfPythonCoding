
def main():
    print('Welcome to the tip calculator')
    total_bill = float(input('What was the total bill?'))
    number_people = int(input('How many people to split the bill?'))
    percentage = int(input('What percentage tip would you like to give? 10, 12 or 15?'))

    # Calculate the tip amount
    tip_amount = total_bill * (percentage / 100)

    # Calculate the total bill with the tip included
    total_with_tip = total_bill + tip_amount

    # Calculate the individual payment for each person
    individual_pay = total_with_tip / number_people

    print(f'Tip amount: ${tip_amount:.2f}')
    print(f'Total bill with tip: ${total_with_tip:.2f}')
    print(f'Each person should pay: ${individual_pay:.2f}')

if __name__ == '__main__':
    main()