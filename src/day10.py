def check1(cycle, X, current_sum):
    if (cycle-20)%40 == 0:
        return (current_sum + (cycle*X))
    return (current_sum)

def check2(cycle, X, output):
    sprite_position = [X-1, X, X+1]
    if (cycle-1) in sprite_position:
        output.append('#')
    else:
        output.append('.')
    if cycle%40 == 0:
        print(*output, sep='')
        output = []
        cycle = 0
    return (cycle, output)

fp = open('data/day10-input.txt')
input = fp.read().split('\n')

X = 1
cycle1 = 0
cycle2 = 0
sum = 0
print_row = []


for line in input:
    instruction = line.split(' ')
    cycle1 +=1
    cycle2 +=1
    if instruction[0] == 'noop':
        sum = check1(cycle1,X, sum)
        cycle2, print_row = check2(cycle2, X, print_row)
    elif instruction[0] == 'addx':
        sum  = check1(cycle1,X, sum)
        cycle2, print_row = check2(cycle2, X, print_row)
        cycle1+=1
        cycle2+=1
        sum  = check1(cycle1,X, sum)
        cycle2, print_row = check2(cycle2, X, print_row)
        X += int(instruction[1])
        
print('answer to part 1 =', sum)