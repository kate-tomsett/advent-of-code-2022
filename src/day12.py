import string

def get_visible(current, path):
    visible = [[current[0]+1, current[1]], [current[0]-1, current[1]], [current[0], current[1]+1], [current[0], current[1]-1]]
    
    remove_list = []
    
    for coord in visible:
        if coord[0] < 0 or coord[1] < 0 or coord[0] > num_rows-1 or coord[1] > num_cols-1:
            remove_list.append(coord)
        if coord in path:
            remove_list.append(coord)
    
    visible = [i for i in visible if i not in remove_list]
    
    return visible
    

def check_movement(current, current_path, visible, grid, solutions):
    current_value = grid[current[0]][current[1]]
    current_path.append(current)
    print('value', current_value, 'at', current[0], ',', current[1])
    print('visible:', visible) 
    for coord in visible:
        coord_value = grid[coord[0]][coord[1]]
        if alphabet.index(coord_value) < alphabet.index(current_value)+1:
            solutions = check_movement(coord, current_path, get_visible(coord, current_path), grid, solutions)
    if current == E:
        print('found the end with path', current_path)
        solutions.append(current_path)
    return solutions


fp = open('test-input.txt')
 
rows = fp.read().split('\n')

alphabet = list(string.ascii_letters)

grid = []
S = [0,0]
E = [0,0]
current = [0, 0]

solutions = []
solutions_found = False

num_rows = len(rows)
num_cols = len(rows[0])

for row in range(0, num_rows):
    grid.append([])
    for col in range(0, num_cols):
        grid[row].append(rows[row][col])
        if rows[row][col] == 'S':
            S = [row, col]
            current = [row, col]
            grid[row][col] = 'a'
        elif rows[row][col] == 'E':
            E = [row, col]
            grid[row][col] = 'z'

current_path = []

while not solutions_found:
    visible = get_visible(current, current_path)
    solutions = check_movement(current, current_path, visible, grid, solutions)
        
    print(visible)
    solutions_found = True
   

