n = int(input())

def second_largest(n):
    for n in range(0,n):
        a = map(int, input().split(' '))
        print(sorted(a)[len(list(a)) - 2])

second_largest(n)