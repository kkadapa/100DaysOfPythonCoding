
def main():
    print('Welcome to Treasure Island!')

    print('Your mission is to find treasure.')

    step1 = input('Left or Right?')

    if step1 == 'Right':
        print('Game Over!')
    else:
        step2 = input('Swim or Wait?')
        if step2 == 'Swim':
            print('Game Over')

if __name__ == '__main__':
    main()