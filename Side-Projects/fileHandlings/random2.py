output = open("./random2_1.txt", "w")

with open("./random2.txt", "r") as file:
    for line in file:
        j = 0 # index where last "   " appeared
        for i in range(0, len(line)-2):
            if line[i] == line[i+1] == line[i+2] == " ":
                output.write(f"{line[j:i]}\n")
                j = i + 3