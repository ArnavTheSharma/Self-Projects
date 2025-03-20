# # Takes 2 sets (1 of which is: {aabb, abab, abba, abbb, abbc, abcb, acbb, baab, baba, babb, babc, bacb, bbaa, bbab, bbac, bbba, bbbb, bbbc, bbca, bbcb, bcab, bcba, bcbb, bcbc, cabb, cbab, cbba, cbbb, cbbc, cbcb})
# # Outputs terms which are in 1 but not the other

# output = open("./random5_1.txt", "w")

# with open("./random5.txt", "r") as file:
#     lines = [line.rstrip() for line in file]
#     # print(lines)
#     set1 = set(lines[0].strip().split(", "))
#     set2 = set(lines[1].strip().split(", "))
#     print(set1)
#     print(set2)
    
#     set1 = {item.strip() for item in set1}
#     set2 = {item.strip() for item in set2}

#     set3 = set1 - set2
#     string = ", ".join(set3)
#     output.write(string)



list1 = []
list2 = []
list3 = []
list4 = []
list5 = []
list6 = []

def itoa(x, base):
    negative = False
    s = ""

    
    negative = (x < 0)
    if negative:
        x = -x
    
    while x != 0:
        # Add char to front of s
        s = str(x % base) + s 
        
        # Integer division gives quotient
        x = x // base 
    
    if negative:
        s = "-" + s

    return s

def binaryGenerator(n):
    binary_list = []
    bit_length = len(bin(n)[2:])  # Define bit_length based on n

    for i in range(1, n+1):
        a = "".join(list(bin(i)[2:].zfill(bit_length)))  # Convert to binary string
        # print(a, end=" ")  # Print each binary number as a list
        if a[5] == "1":
            list1.append(int(a, 2)+1) 
        if a[4] == "1":
            list2.append(int(a, 2)+1)
        if a[3] == "1":
            list3.append(int(a, 2)+1)
        if a[2] == "1":
            list4.append(int(a, 2)+1)
        if a[1] == "1":
            list5.append(int(a, 2)+1)
        if a[0] == "1":
            list6.append(int(a, 2)+1)
        

        binary_list.append(a)
    
    return binary_list



n = 63
binary_numbers = binaryGenerator(n)

print("List 1:", list1)
print("List 2:", list2)
print("List 3:", list3)
print("List 4:", list4)
print("List 5:", list5)
print("List 6:", list6)
