n,k = input().split()

n = int(n)
k = int(k)

def divisibles_by_k(n,k):    
    answer = 0
    for i in range(n):
        number = int(input())
        if number % k == 0:
            answer = answer + 1
    print(answer)

divisibles_by_k(n,k)