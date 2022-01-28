t = int(input())

for i in range(t):  
    low, high = map(int, input().split())
    ans = 0
    for k in range(low,high+1):
        if k % 10 == 2 or k % 10 == 3 or k % 10 == 9:
            ans += 1
    print(ans)