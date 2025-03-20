output = open("./random1_2.txt", "a")


with open("./random1.txt", "r") as file:
    for lines in file:
        output.write(lines[3:])