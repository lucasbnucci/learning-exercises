def highest_divisor_10(number):
    i = 10
    while i > 0:
        if number % i == 0:
            print(i)
            break
        else:
            i -= 1

number = int(input())

highest_divisor_10(number)