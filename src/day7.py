class Tree:
    def __init__(self, data, size):
        self.data = data
        self.nodes = []
        self.size = size
        
    def addNode(self, data, size):
        self.nodes.append(Tree(data, size))
        return len(self.nodes)-1

def sendTreeBack(startTree, currentTree, path):
    currentTree = startTree
    for index in path:
        currentTree = currentTree.nodes[index]
    return(currentTree)
    
def calcSum(currentTree, accumulatedSum, maxSize):
    for node in currentTree.nodes:
        nodeSum, newSum = calcSum(node, accumulatedSum, maxSize)
        accumulatedSum = newSum
        currentTree.size += nodeSum
    if currentTree.size <= maxSize and len(currentTree.nodes)!=0:
        accumulatedSum += currentTree.size
    return currentTree.size, accumulatedSum       

def findDir(currentTree, currentDir, space):
    for node in currentTree.nodes:
        currentDir = findDir(node, currentDir, space)
    if currentTree.size >= space and currentTree.size < currentDir and len(currentTree.nodes)!=0:
        currentDir = currentTree.size
    return currentDir    

fp = open('day7-input.txt')

lines = fp.read().split('\n')

startTree = Tree('/', 0)
currentTree = startTree
path = []
myPath = 0

for line in lines:
    input = line.split(' ');
    if (input[1] == 'cd'):
        if (input[2] == '/'):
            path = []
        elif(input[2] == '..'):
            path.pop()
            currentTree = sendTreeBack(startTree, currentTree, path)
        else:
            newPath = currentTree.addNode(input[2], 0)
            currentTree = currentTree.nodes[newPath]
            path.append(newPath)
    if input[0].isnumeric():
        currentTree.addNode(input[1], int(input[0]))

totalSize = 0
calculatedSum = 0
maxSize = 100000

totalSize, calculatedSum = calcSum(startTree, calculatedSum, maxSize)

print('Total size', totalSize)
print('Calculated sum', calculatedSum)

spaceNeeded = 30000000 - (70000000 - totalSize)
print('Space needed', spaceNeeded)

chosenDir = totalSize

chosenDir = findDir(startTree, chosenDir, spaceNeeded);

print('Size of directory to delete', chosenDir)