#a = number of bombarded particles
#n = limit of particles before passing to next and going to 0
#k = number of rooms 

a, n, k = map(int, input().split())

answer = []
remainder = a
for i in range(k):
    answer.append(remainder % (n+1))
    remainder = remainder // (n+1)

print(*answer)