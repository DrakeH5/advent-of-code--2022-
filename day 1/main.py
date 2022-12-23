input = open("input.txt", "r").read() 

cals = [""]
input = input.replace("\n\n", "~")
input = input.replace("\n", "N")
for i in range(int(len(input))):
    if input[i] == "N":
        cals.append("")
    elif input[i] == "~":
        cals.append("~")
        cals.append("")
    else: 
        cals[len(cals)-1] += str(input[i])

eachElf = [0]
for i in range(int(len(cals))):
    if cals[i] != "~" and len(cals[i])>0:  
        eachElf[len(eachElf)-1]+= int(float(cals[i]))
    else: 
        eachElf.append(0)
output = 0
for i in eachElf:
    if i > output: 
        output = i
print(output)