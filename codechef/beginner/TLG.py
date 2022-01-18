n = int(input())

def winner_tlg(n):
    scores = []
    total_score = 0
    for i in range(0,n):
       player1, player2 = map(int, input().split())
       scores.append(int(player1 - player2 + total_score))
       total_score += player1 - player2
    if (sorted(scores)[0] + sorted(scores)[len(scores) - 1]) > 0:
       print("1 ",sorted(scores)[len(scores) - 1]) #player1 wins
    else:
       print("2 ",abs(sorted(scores)[0])) #player2 wins

winner_tlg(n)