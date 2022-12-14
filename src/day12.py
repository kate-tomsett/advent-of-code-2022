fp = open('test-input.txt')
 
rows = fp.read().split('\n')

grid = []
S_row = 0
S_col = 0
E_row = 0
E_col = 0
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
            S_row = row
            current = [row, col]
            S_col = col
        elif rows[row][col] == 'E':
            E_row = row
            E_col = col

while !solutions_found:
    visable =