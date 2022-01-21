n = int(input())

for i in range(n):
    number_of_horses = int(input().strip(' '))
    horses_skills = sorted(list(map(int, input().split())))
    answer = 10000000000
    for k in range(len(horses_skills) - 1):
        if (horses_skills[k+1] - horses_skills[k]) < answer:
            answer = horses_skills[k+1] - horses_skills[k]
    print(int(answer))