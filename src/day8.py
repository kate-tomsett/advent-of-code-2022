def is_row_wise_hidden(input, row, col, height):
    #LEFT
    hidden_from_left = False
    
    for i in range(0, col):
        if input[row][i] >= height:
            hidden_from_left = True
            break
        
    #RIGHT
    hidden_from_right = False
    
    for i in range(col+1, len(input[0])):
        if input[row][i] >= height:
            hidden_from_right = True
            break

    return(hidden_from_left and hidden_from_right)
    
def is_column_wise_hidden(input, row, col, height):
    #TOP
    hidden_from_top = False
    
    for i in range(0, row):
        if input[i][col] >= height:
            hidden_from_top = True
            break
        
    #BOTTOM
    hidden_from_bottom = False
    
    for i in range(row+1, len(input)):
        if input[i][col] >= height:
            hidden_from_bottom = True
            break

    return (hidden_from_top and hidden_from_bottom)
    
def calculate_scenic_score(input, row, col, height):
    #LEFT
    left_score = 0
    for i in range(col-1, -1, -1):
        left_score+=1
        if input[row][i] >= height:
            break
    
    #RIGHT
    right_score = 0
    for i in range(col+1, len(input[0])):
        right_score+=1
        if input[row][i] >= height:
            break    

    #UP
    up_score = 0
    for i in range(row-1, -1, -1):
        up_score+=1
        if input[i][col] >= height:
            break     

    #DOWN
    down_score = 0
    for i in range(row+1, len(input)):
        down_score+=1
        if input[i][col] >= height:
            break       
    
    return (left_score * right_score * up_score * down_score)
    
fp = open('data/day8-input.txt')

inputLines = fp.read().split('\n')
inputMatrix = []
for line in inputLines:
    inputMatrix.append(line)

numHidden = 0
currentScenicScore = 0

for row in range(0, len(inputMatrix)):
    for col in range(0, len(inputMatrix)):
        height = inputMatrix[row][col]
        if (is_row_wise_hidden(inputMatrix, row, col, height) and is_column_wise_hidden(inputMatrix, row, col, height)):
            numHidden+=1
        newScenicScore = calculate_scenic_score(inputMatrix, row, col, height)
        if (newScenicScore > currentScenicScore):
            currentScenicScore = newScenicScore
            
numVisible = len(inputMatrix)*len(inputMatrix[0]) - numHidden
print('num visible =', numVisible)
print('largest scenic score=', currentScenicScore)