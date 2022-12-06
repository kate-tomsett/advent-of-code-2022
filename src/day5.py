fp = open('data/day5-input.txt')

lines = fp.read().split('\n')
startLine = 0
numStacks = 0

for line in lines:
    if line.find(' 1') == 0:
        startLine = lines.index(line)
        numStacks = int(line[len(line)-2])

stacks1 = [ [] for _ in range(numStacks) ]
stacks2 = [ [] for _ in range(numStacks) ]

for i in range(startLine-1, -1, -1):
    for j in range(0, len(lines[i])):
        if lines[i][j].isalpha():
            stack = int((j - 1) / 4)
            stacks1[stack].append(lines[i][j])
            stacks2[stack].append(lines[i][j])

for i in range(startLine+2, len(lines)):
    instruction = lines[i].split(' ')
    for j in range(0, int(instruction[1])):
        moving = stacks1[int(instruction[3])-1].pop()
        stacks1[int(instruction[5])-1].append(moving)

answer1 = ""

for stack in stacks1:
    answer1 = answer1 + stack.pop()
    

for i in range(startLine+2, len(lines)):
    instruction = lines[i].split(' ')
    spare = []
    for j in range(0, int(instruction[1])):
        moving = stacks2[int(instruction[3])-1].pop()
        spare.append(moving)
    for k in range(0, int(instruction[1])):
        gone = spare.pop()
        stacks2[int(instruction[5])-1].append(gone)

answer2 = ""

for stack in stacks2:
    answer2 = answer2 + stack.pop()
   
print(answer1)
print(answer2)
fp.close
