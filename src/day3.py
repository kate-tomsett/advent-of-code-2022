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

fp.close