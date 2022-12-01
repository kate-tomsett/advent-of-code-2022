
fp = open('data/day1-input.txt')
elves = []
calories = 0

# Read in and sum up calories that each elf is carrying. 
# len(elves) - number of elves in the jungle
for line in fp:
    if line != '\n':
        calories = calories + int(line)
    else:
        elves.append(calories)
        calories = 0
    
    
# Sort total number of calories per elf into ascending order
elves.sort()

total = 0

# Part 1 - Elf carry the most calories
print('Answer to part 1 is: ', elves[len(elves) - 1])

# Part 2 - Total calories being carried by the 3 elves carrying the most
for elf in range(1, 4):
    total = total + elves[len(elves) - 1 - elf]  
print('Answer to part 2 is: ', total)