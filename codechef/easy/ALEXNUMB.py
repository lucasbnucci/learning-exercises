def factorial(n):
    number = n
    for i in range(1,n):
        number = (number*i)
    return number

t = int(input())

for i in range(t):
    n_of_digits = int(input())
    list_of_numbers = list(list(dict.fromkeys(map(int,input().split(' ')))))
    print(factorial(len(list_of_numbers))//(2*(factorial(len(list_of_numbers)-2))))