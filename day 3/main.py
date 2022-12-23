input = open("input.txt", "r").read() 

rucksacks = [""]
input = input.replace("\n", "~")
for i in range(int(len(input))):
    if input[i] == "~":
        rucksacks.append("")
    else: 
        rucksacks[len(rucksacks)-1] += str(input[i])

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

allRepeats = ""

for i in range(len(rucksacks)):
    for j in range(52):
        if int(rucksacks[i].find(letters[j], 0, int(len(rucksacks[i])/2))) > -1:
            search = rucksacks[i].find(letters[j], int(len(rucksacks[i])/2), int(len(rucksacks[i])))
            if search > -1:
                allRepeats+=rucksacks[i][search]

total = 0
for i in range(len(allRepeats)):
    for j in range(len(letters)):
        if allRepeats[i] == letters[j]:
            total+=j+1

print(total)