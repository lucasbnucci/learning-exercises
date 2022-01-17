n = int(input())

def reverse_number(n):
    for n in range(0,n):
        number = str(input())
        answer = ''
        for digit in range(0,len(number)):
            answer += number[((len(number) - digit - 1))]
        print(int(answer))

reverse_number(n)

#Again, just saw a solution online that used algorithms: get the remainder of the division by 10, add and divide the number by then, rinse and repeat. Not sure how to evaluate which of the solutions are faster