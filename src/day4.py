fp = open('data/day4-input.txt')

elfPairs = fp.read().split('\n')

numFullyContained = 0
numOverlaps = 0

for elfPair in elfPairs:
    #Part 1
    
    #Get sections assignments for each elf in the pair
    #Get start and end section IDs for each elf
    elf1, elf2 = elfPair.split(',')
    elf1start, elf1end = elf1.split('-')
    elf2start, elf2end = elf2.split('-')
   
    #Create range form elfstart to elfend + 1, e.g. range(2, 5) = [2, 3, 4] for 2-4
    #This converts 2-4 format to [2, 3, 4] list format for each elf. 
    elf1Range = list(range(int(elf1start), int(elf1end)+1))
    elf2Range = list(range(int(elf2start), int(elf2end)+1))
    
    #bool1 will return true if every element in elf1Range is present in elf2Range, so elf1Range is fully contained
    #bool2 will return true if every element in elf2Range is present in elf1Range, so elf2Range is fully contained
    bool1 = all([item in elf2Range for item in elf1Range])
    bool2 = all([item in elf1Range for item in elf2Range])
    
    #Increment number of fully contained assignemnts if either elf1Range or elf2Range is fully contained
    if (bool1 or bool2):
        numFullyContained += 1
    
    #Part 2
    
    #If the intersection of the two ranges is not zero, i.e. any element ovelaps, increment numOverlaps
    if (set(elf1Range).intersection(set(elf2Range))):
        numOverlaps += 1

print('Answer to part 1 =' , numFullyContained)

print('Answer to part 2 =' , numOverlaps)

fp.close