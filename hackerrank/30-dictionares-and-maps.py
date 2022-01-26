numbers = {}
n = int(input())

for i in range(n):
    name, phone = map(str, input().split(' '))
    if name in numbers:
        next
    numbers[name] = int(phone)

for i in range(n):
    try:
        who = input()
    except EOFError as e: #The code only run when I did this, found that on forum. Need to learn what this does, tho.
        break
    if who in numbers:
        print(who,'=',numbers[who], sep='')
    else:
        print('Not found')