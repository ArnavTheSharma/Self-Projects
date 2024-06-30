# credit to umass amherst cics110 team for the idea:

# This cipher creates two substrings from the message:
# s1: comprises of all the characters at odd indices
# s2: comprises of all the characters at even indices. It then joins (concatenates) the s2 to s1. This is the required encoding
# as an example, abcd generated bd and ac, and the output is bdac

def encrypt(word):
    s1 = s2 = ""
    n = 0
    for i in word:
        if n%2 == 0:
            s1 = s1 + i
        else:
            s2 = s2 + i
        n += 1
    return str(s1 + s2)

def decrypt(word):
    n = len(word)
    for i in range(0, n//2):
        print(word[i] + word[i+n//2], end="")

message = str(input("What word do you want to encrypt and decrypt? "))
print(encrypt(message))
decrypt(encrypt(message))