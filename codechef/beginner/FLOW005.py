#smallest number of notes

def smallest_number_of_notes(n): 
    notes = [100, 50, 10, 5, 2, 1]
    for j in range(0,n):
        answer = 0
        money = int(input())
        for i in range(0,len(notes)):
            if money >= notes[i]:
                answer += int(money/notes[i])
                money = int(money%notes[i])
                if money == 0:
                    print(answer)

n = int(input()) 

smallest_number_of_notes(n)