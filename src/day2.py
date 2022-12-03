fp = open('data/day2-input.txt')

rounds = fp.read().split('\n')

elfShapes = ['A', 'B', 'C']
myShapes = ['X', 'Y', 'Z']

# my Lose Win Draw if elf choses Rock Paper Scissors
elfOutcomes = [[2, 0, 1],[0, 1, 2],[1, 2, 0]]

# Lose Draw Win
Outcomes = [0,3,6]

scorePart1 = 0
scorePart2 = 0

for round in range(0, len(rounds)):
    # Get 1st and 2nd value for each round
    draws = rounds[round].split(' ')
    
    # Part 1
    elf = elfShapes.index(draws[0])
    me = myShapes.index(draws[1])
    
    # Add 1, 2, or 3 for if I chose Rock Paper or Scissors
    scorePart1 = scorePart1 + (me + 1)
    
    # Add the Lose Draw or Win points
    scorePart1 = scorePart1 + Outcomes[elfOutcomes[elf].index(me)]
    
    # Part 2
    # 0 for lose, 1 for draw, 2 for win
    outcome = myShapes.index(draws[1])
    
    # Find what I would need to choose to get that outcome
    me = elfOutcomes[elf][outcome]
    
    # Add 1, 2, or 3 for if I chose Rock Paper or Scissors
    scorePart2 = scorePart2 + (me + 1)
    
    # Add the Lose Draw or Win points
    scorePart2 = scorePart2 + Outcomes[outcome]
    
print('Answer to part 1 =', scorePart1)
print('Answer to part 2 =', scorePart2)


fp.close

