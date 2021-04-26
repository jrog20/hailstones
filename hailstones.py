"""
File: hailstones.py
"""
import math

def main():
    n = int(input('Enter a number: '))
    count = 0

    while n != 1:
        if n % 2 == 0:
            print(str(n) + ' is even, so I take half: ' + str(int(n/2)))
            n //= 2
            count += 1
        else:
            print(str(n) + ' is odd, so I make 3n + 1: ' + str(n * 3 + 1))
            n = (n * 3) + 1
            count += 1

    print('This process took ' + str(count) + ' steps to reach 1')


if __name__ == '__main__':
    main()
