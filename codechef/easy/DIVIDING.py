n = int(input())

number_of_members = n
total_stamps = sum(list(map(int,input().split(' '))))

for i in range(number_of_members):
    total_stamps -= n
    n -= 1

if total_stamps == 0:
    print("YES")
else:
    print("NO")