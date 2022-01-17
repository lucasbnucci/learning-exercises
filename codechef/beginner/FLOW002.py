n = int(input().strip())

def remainder(n):
    for i in range(0,n):
        (a, b) = map(int, input().split())
        answer = (a % b)
        print(answer)

remainder(n)