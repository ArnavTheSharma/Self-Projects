# old inneficient code:

# def function(line, word):
#     found = False

#     for i in range(0, len(line) - len(word) + 1): # iterate through entire line
#         if line[i] == word[0]: # checks if any character in line has starting letter of word
#             n = i
#             found = True
#             for j in range(0, len(word)): # iterate through word
#                 if line[n+j] != word[j]: 
#                     found = False 
#                     continue # this will continue the nested loop, not outer loop
#             if found == False: 
#                 continue # this will continue the outer loop
#             #found = True # return final answer as True if outer loop wasn't continued
#     return found


# a = "this is a line with word"
# b = "line"
# c = "worl"
# print(function(a, b))
# print(function(a, c))


def function(line, word):
    found = False

    for i in range(0, len(line) - len(word) + 1): 
            found = True
            for j in range(0, len(word)): 
                if line[i+j] != word[j]: 
                    found = False 
                    break
            if found == True: 
                break 
    return found

            

a = "this is a line with word"
b = "line"
c = "worl"
d = "is a"
print(function(a, b))
print(function(a, c))
print(function(a, d))

