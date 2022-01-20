n = int(input())

def rectangle(n):
    for i in range(n):
        sides = sorted(list(map(int, input().split(' '))))
        if sum(sides) % 2 != 0:
            print("NO")
            continue
        if sides[0] == sides[1] and sides[2] == sides[3]:
            print("YES")
        else:
            print("NO")

rectangle(n)