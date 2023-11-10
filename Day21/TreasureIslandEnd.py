
def main():
    print('Welcome to Treasure Island!')

    print('Your mission is to find treasure.')

    step1 = input('Left or Right?\n')

    if step1 == 'Right':
        print('Game Over!')
    else:
        step2 = input('Swim or Wait?\n')
        if step2 == 'Swim':
            print('Game Over')
        else:
            step3 = input('Which door Red or Blue or Yellow?\n')
            if step3 == 'Red':
                print('Game Over')
            elif step3 == 'Blue':
                print('Game Over')
            else:
                print('You Win!')


if __name__ == '__main__':
    main()