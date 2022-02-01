t = int(input())

for i in range(t):
    number_of_songs = int(input())
    list_of_songs = list(map(int, input().split(' ')))[:number_of_songs]
    position_johnny = int(input())
    ans = list_of_songs[position_johnny - 1]
    list_of_songs.sort()
    print(list_of_songs.index(ans) + 1)