T = int(input())

for i in range(T):
    total_of_items, firstbag = map(int, input().split())
    secondbag = total_of_items - firstbag
    items = sorted(list(map(int, input().split())))
    if firstbag >= secondbag:
        answer = sum(items[secondbag:total_of_items]) - sum(items[0:secondbag])
    else:
        answer = sum(items[firstbag:total_of_items]) - sum(items[0:firstbag])
    
    print(answer)

