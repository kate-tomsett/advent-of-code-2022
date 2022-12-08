fp = open('day6-input.txt')

input = fp.read()
marker = 0

for character in range(0, len(input)-3):
    subInput = input[character:character+4]
    
    inArray = set()
    repeated = set()
    
    for char in subInput:
        if char not in inArray:
            inArray.add(char)
        else:
            repeated.add(char)
    
    if not repeated:
        marker = character+4
        break

print('Part 1 - characters received before first marker:', marker)

marker = 0

for character in range(0, len(input)-13):
    subInput = input[character:character+14]
    
    inArray = set()
    repeated = set()
    
    for char in subInput:
        if char not in inArray:
            inArray.add(char)
        else:
            repeated.add(char)
    
    if not repeated:
        marker = character+14
        break

print('Part 2 - characters received before first marker:', marker)