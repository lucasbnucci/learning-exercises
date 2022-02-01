n = int(input())

for i in range(n):
    count_numbers = int(input())
    a = list(map(int, input().split()))
    while max(a) != min(a):
        a[a.index(max(a))] = max(a) - min(a)
    print(a[0]) 

#So, this solve the problem but the code won't run on time. This is the second time I encounter this kind of problem, I could reduce the interactions with greatest common divisor. It's a good catch but the solutions are more math than actual coding. Might be time to get back to studying math/coding (?)