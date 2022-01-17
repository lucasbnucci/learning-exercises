from math import sqrt

n = int(input())

def square_round_down(n):
    for i in range(0,n):
        number = int(input())
        print(int(sqrt(number)))

square_round_down(n)