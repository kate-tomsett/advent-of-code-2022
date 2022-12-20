fp = open('test-input.txt')

inputs = fp.read().split('\n')
result = []
original = []

for input in inputs:
    result.append(len(original))
    original.append(int(input))

for i in range(0, len(original)):
    currentIndex = result.index(i)
    print('current element =', original[i], 'currentIndex in result =', currentIndex)
    moveTo = currentIndex + original[i]
    print('first moveTo =', moveTo)
    while moveTo >= len(original):
        print(moveTo%len(original))
        print(moveTo%len(original)-1)
        moveTo = moveTo - (len(original)-1)
        print('thats more than', len(original)-1, 'moveTo is now', moveTo)
    while moveTo < 0:
        print(moveTo%len(original))
        print(moveTo%len(original)-1)
        moveTo = moveTo + (len(original)-1)
        print('thats less than 0 moveTo is now', moveTo)
    print('final moveTo =', moveTo)
    result.insert(moveTo, result.pop(currentIndex))
    print([original[j] for j in result])

indexOf0inOrig = original.index(0)
num = len(original) - result.index(indexOf0inOrig);
print(num)
    
coord1 = original[result[(1000-num)%len(original)]]
coord2 = original[result[(2000-num)%len(original)]]
coord3 = original[result[(3000-num)%len(original)]]

print(coord1, coord2, coord3)

answer1 = coord1 + coord2 + coord3
print('Answer to part 1 =', answer1)
