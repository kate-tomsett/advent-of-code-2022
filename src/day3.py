import string

fp = open('data/day3-input.txt')

rucksacks = fp.read().split('\n')

#List of alphabet values lowercase then uppercase, e.g 'a, b, ... , y, z, A, B, ... , Y, Z'
alphabet = list(string.ascii_letters)

prioritySum = 0

for rucksack in rucksacks:
    #Split contents of each rucksack into it's two compartments
    half_length = int(len(rucksack)/2)
    compartment1, compartment2 = rucksack[:half_length], rucksack[half_length:]
    
    #Convert each compartment to sets and find the intersection, the elements contained in both compartments, without duplicates
    set1 = set(compartment1)
    set2 = set(compartment2)
    commonElements = list(set1.intersection(set2))   
    
    #Sum the respective priority for each element contained in both compartments
    for element in commonElements:
        prioritySum = prioritySum+ (alphabet.index(element) + 1)
    
print("Answer to part 1 =", prioritySum)

badgeSum = 0

for i in range(0, len(rucksacks), 3):
    #Get groups of three rucksacks
    rucksack1 = set(rucksacks[i])
    rucksack2 = set(rucksacks[i+1])
    rucksack3 = set(rucksacks[i+2])
    
    #Find the element contained in all three rucksacks
    badges = rucksack1.intersection(rucksack2, rucksack3)        

    #Have to do this to access a string in a set
    #Add the priority of the common badge to the sum
    for badge in badges:
        badgeSum = badgeSum + (alphabet.index(badge) + 1)

print("Answer to part 2 =", badgeSum)

fp.close