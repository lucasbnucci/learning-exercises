n = int(input())

def tlg2(n):
   player1 = 0
   player2 = 0
   max_diference = 0
   for n in range(0,n):
      a = list(map(int, input().split(' ')))
      player1 += a[0]
      player2 += a[1]
      if abs(player1 - player2) > abs(max_diference):
         max_diference = player1 - player2
   if max_diference > 0:
      print("1 ",abs(max_diference))
   else:
      print("2 ",abs(max_diference))

tlg2(n)