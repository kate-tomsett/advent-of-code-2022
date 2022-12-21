import string

def get_visible(current):
    visible = [[current[0]+1, current[1]], [current[0]-1, current[1]], [current[0], current[1]+1], [current[0], current[1]-1]]
    
    remove_list = []
    
    for coord in visible:
        if coord[0] < 0 or coord[1] < 0 or coord[0] > num_rows-1 or coord[1] > num_cols-1:
            remove_list.append(coord)
    
    visible = [i for i in visible if i not in remove_list]
    
    return visible
    
def shortest_path(grid, start, end):
    paths = [[start]]
    path_index = 0
    end_val = grid[end[0]][end[1]]

    previous = [start]
    
    while path_index < len(paths):
        current_path = paths[path_index]
        last = current_path[-1]
        current_val = grid[last[0]][last[1]]
        #print('current_val', current_val, last)
        next_nodes = get_visible(last)
        
        if end in next_nodes and (alphabet.index(end_val) <= alphabet.index(current_val)+1):
            return current_path
        
        for node in next_nodes:
            if not node in previous:
                node_val = grid[node[0]][node[1]]
                #print('node_val', node_val, node)
                if (alphabet.index(node_val) <= alphabet.index(current_val)+1):
                    new_path = current_path[:]
                    new_path.append(node)
                    paths.append(new_path)
                    previous.append(node)
        
        path_index += 1
    return [0]*(len(grid) * len(grid[0]))

fp = open('day12-input.txt')
 
rows = fp.read().split('\n')

alphabet = list(string.ascii_letters)

grid = []
As = []
E = [0,0]
current = [0, 0]

num_rows = len(rows)
num_cols = len(rows[0])

for row in range(0, num_rows):
    grid.append([])
    for col in range(0, num_cols):
        grid[row].append(rows[row][col])
        if rows[row][col] == 'a' or rows[row][col] == 'S':
            As.append([row, col])
            grid[row][col] = 'a'
        elif rows[row][col] == 'E':
            E = [row, col]
            grid[row][col] = 'z'

final_solution = [0] * (num_cols * num_rows)
current_solution = []


for start_point in As:
    current_solution = shortest_path(grid, start_point, E)
    if len(current_solution) < len(final_solution):
        final_solution = current_solution.copy()
        
print('Answer to part 2 -', len(final_solution))