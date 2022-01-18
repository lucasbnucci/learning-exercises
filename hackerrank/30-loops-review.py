n = int(input())

def separate_words(n):
    for i in range(0,n):
        odd = "" # for every letter N / 2 + 1
        even = "" #for every letter N / 2 
        word = str(input())
        k = 0
        while k < len(word):
            if k % 2 == 0:
                even += word[k]
                k += 1
            else:
                odd += word[k]
                k += 1
        print(even,odd)

separate_words(n)