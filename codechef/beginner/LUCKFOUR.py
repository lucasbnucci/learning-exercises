n = int(input())

def count_four(n):
    for i in range(0,n):
        number = str(input())
        answer = 0
        for digit in number:
            if int(digit) == 4:
                answer += 1
        print(answer)

count_four(n)