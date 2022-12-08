def isRowWiseHidden(input, row, col, height):
    #LEFT
    safeFromLeft = False
    
    for i in range(0, col):
        if input[row][i] >= height:
            safeFromLeft = True
            break
        
    #RIGHT
    safeFromRight = False
    
    for i in range(col+1, len(input[0])):
        if input[row][i] >= height:
            safeFromRight = True
            break

    return(safeFromLeft and safeFromRight)
    
def isColumnWiseHidden(input, row, col, height):
    #TOP
    safeFromTop = False
    
    for i in range(0, row):
        if input[i][col] >= height:
            safeFromTop = True
            break
        
    #BOTTOM
    safeFromBottom = False
    
    for i in range(row+1, len(input)):
        if input[i][col] >= height:
            safeFromBottom = True
            break

    return (safeFromTop and safeFromBottom)
    
def calcScenicScore(input, row, col, height):
    #LEFT
    leftScore = 0
    for i in range(col-1, -1, -1):
        leftScore+=1
        if input[row][i] >= height:
            break
    
    #RIGHT
    rightScore = 0
    for i in range(col+1, len(input[0])):
        rightScore+=1
        if input[row][i] >= height:
            break    

    #UP
    upScore = 0
    for i in range(row-1, -1, -1):
        upScore+=1
        if input[i][col] >= height:
            break     

    #DOWN
    downScore = 0
    for i in range(row+1, len(input)):
        downScore+=1
        if input[i][col] >= height:
            break       
    
    return (leftScore * rightScore * upScore * downScore)
    
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
        if (isRowWiseHidden(inputMatrix, row, col, height) and isColumnWiseHidden(inputMatrix, row, col, height)):
            numHidden+=1
        newScenicScore = calcScenicScore(inputMatrix, row, col, height)
        if (newScenicScore > currentScenicScore):
            currentScenicScore = newScenicScore
            
numVisible = len(inputMatrix)*len(inputMatrix[0]) - numHidden
print('num visible =', numVisible)
print('largest scenic score=', currentScenicScore)