n = int(input())
for i in range(n):
    number_of_games = int(input())
    for j in range(number_of_games):
        initial_head_or_tails, total_rounds_coins, count_red_or_tails = map(int, input().split(' '))
        if initial_head_or_tails != count_red_or_tails:
            print(total_rounds_coins//2 + total_rounds_coins % 2)
        else:
            print(total_rounds_coins - (total_rounds_coins//2 + total_rounds_coins % 2))