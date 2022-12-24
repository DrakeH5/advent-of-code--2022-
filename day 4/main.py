input = open("input.txt", "r").read().splitlines()

results = 0
for i in input: 
    elf1,elf2 = i.split(",")
    e1n1, e1n2 = [int(r) for r in elf1.split("-")]
    e2n1, e2n2 = [int(r) for r in elf2.split("-")]

    if e1n1 <= e2n1 and e1n2>=e2n2:
        results+=1
    elif e2n1 <= e1n1 and e2n2>=e1n2: 
        results+=1
print(results)