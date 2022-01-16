n = int(input().strip())

def sumofdigits(n):
    for i in range(0,n):
        number = int(input().strip())
        answer = 0
        for digit in str(number):
            answer = answer + int(digit)
        print(answer)

sumofdigits(n)