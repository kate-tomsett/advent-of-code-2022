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
        print('New directory name =' , currentTree.data)
    return(currentTree)

def displayNodes(currentTree):
    for node in currentTree.nodes:
        print('in directory', currentTree.data, ', current node =', node.data, ', size =', node.size)
        if len(node.nodes) != 0:
            displayNodes(node)

fp = open('test-input.txt')

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
            print('Going back one directory')
            path.pop()
            currentTree = sendTreeBack(startTree, currentTree, path)
            print('New path =', path)            
        else:
            print('Adding dir' , input[2])
            newPath = currentTree.addNode(input[2], 0)
            currentTree = currentTree.nodes[newPath]
            path.append(newPath)
            print('New path =', path)
    if input[0].isnumeric():
        print('Adding' , input[0], 'to path', path)
        currentTree.addNode(input[1], int(input[0]))
 
 
displayNodes(startTree)
