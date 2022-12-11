class Tree:
    def __init__(self, data, size):
        self.data = data
        self.nodes = []
        self.size = size
        
    def add_node(self, data, size):
        self.nodes.append(Tree(data, size))
        return len(self.nodes)-1

def return_to_previous_directory(original_tree, path):
    previous_tree = original_tree
    for index in path:
        previous_tree = previous_tree.nodes[index]
    return(previous_tree)
    
def calc_sum(current_tree, accumulated_sum, max_size):
    for node in current_tree.nodes:
        total_size_of_node, new_sum = calc_sum(node, accumulated_sum, max_size)
        accumulated_sum = new_sum
        current_tree.size += total_size_of_node
    if current_tree.size <= max_size and len(current_tree.nodes)!=0:
        accumulated_sum += current_tree.size
    return current_tree.size, accumulated_sum       

def find_dir_to_delete(current_tree, current_dir_to_delete, space):
    for node in current_tree.nodes:
        current_dir_to_delete = find_dir_to_delete(node, current_dir_to_delete, space)
    if current_tree.size >= space and current_tree.size < current_dir_to_delete and len(current_tree.nodes)!=0:
        current_dir_to_delete = current_tree.size
    return current_dir_to_delete    

fp = open('data/day7-input.txt')

lines = fp.read().split('\n')

original_tree = Tree('/', 0)
current_tree = original_tree
path = []
myPath = 0

for line in lines:
    input = line.split(' ');
    if (input[1] == 'cd'):
        if (input[2] == '/'):
            path = []
        elif(input[2] == '..'):
            path.pop()
            current_tree = return_to_previous_directory(original_tree, path)
        else:
            newPath = current_tree.add_node(input[2], 0)
            current_tree = current_tree.nodes[newPath]
            path.append(newPath)
    if input[0].isnumeric():
        current_tree.add_node(input[1], int(input[0]))

totalSize = 0
calculatedSum = 0
max_size = 100000

totalSize, calculatedSum = calc_sum(original_tree, calculatedSum, max_size)

print('Total size', totalSize)
print('Calculated sum', calculatedSum)

spaceNeeded = 30000000 - (70000000 - totalSize)
print('Space needed', spaceNeeded)

chosenDir = totalSize

chosenDir = find_dir_to_delete(original_tree, chosenDir, spaceNeeded);

print('Size of directory to delete', chosenDir)