n = int(input())

def factoring(n):
    for i in range(0,n):
        number = int(input())
        answer = 1
        for k in range(0,number):
            answer *= (number - k)
        print(answer)

factoring(n)