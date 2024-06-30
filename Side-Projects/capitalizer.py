# capitalizes every 2nd letter in a sentence, just for fun

while True:
    word = str(input("Input your line: "))
    n = 0

    for i in word:
        if n%2 == 0 and n < len(word):
            word = word.replace(word[n], i.capitalize(), 1)
        n += 1
        
    print(word)