n = int(input().strip())

def first_ten_multiples(n):
    for i in range(1,11):
        result = n * i
        print(f'{n} x {i} = {result}')

first_ten_multiples(n)