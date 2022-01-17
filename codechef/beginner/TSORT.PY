n = int(input())

def sort(n):
    numbers = []
    for i in range(0,n):
        numbers.append(int(input()))
    numbers.sort()
    #print(numbers) - to validate if the array is correct 
    for k in range(0,len(numbers)):
        print(numbers[k])

sort(n)