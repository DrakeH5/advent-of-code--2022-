import math

input = open("input.txt", "r").read() 

input = input.replace("\n", "")

stacks = [[],[],[],[],[],[],[],[],[]]
boxes = ""
for i in range(8):
    x=1
    for j in range(9): 
        boxes+=input[x + i*35]
        x+=4

for i in range(72): 
    stacks[(i - (math.trunc(i/9)*9))].append(boxes[i])

print(stacks)
