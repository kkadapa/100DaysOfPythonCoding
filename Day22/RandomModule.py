import random
import mymodule

def main():
    c = random.randint(100, 300)

    print(f'Random number is {c}')
    print(mymodule.pi)

if __name__ == '__main__':
    main()