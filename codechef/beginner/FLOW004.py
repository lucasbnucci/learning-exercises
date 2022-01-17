n = int(input().strip())

def sum_of_first_and_last_digit(n):
    for i in range(0,n):
        number = int(input())
        answer = int(str(number)[0]) + (number % 10) #My initial idea was something like str(number[len[number]]) but the remainder of a division by 10 looked good too. I have to learn how to measure which code is better.
        print(answer)

sum_of_first_and_last_digit(n)