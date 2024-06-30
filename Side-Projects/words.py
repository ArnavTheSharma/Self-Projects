#gamepigeon word anagrams solver. Finds possible words you can make using the spagetti of letters
word = str(input("Enter letters: "))
list = []
for _ in word:
    list.append(_)

# i is the length of the word you're trying to find
# j is each letter in the string you have, under the variable word
# bool is there to ensure the algorithm doesn't count the same letter (same index) twice in a row unless it's in a different index
for i in range(len(word), 2, -1):
    for j in word:
        for k in word:
            bool = True
            if k == j and bool == True:
                bool = False
                continue
            #else:


    
    

#wordle
