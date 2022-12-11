import numpy as np
import math

def calculate_direction(direction):
    if direction == 'R':
        direction_vector = [0,1]
    elif direction == 'L':
        direction_vector = [0,-1]
    elif direction == 'U':
        direction_vector = [1,0]
    else:
        direction_vector = [-1,0]
    return direction_vector

def move(old_position, direction_vector):
    new_position = list(np.add(old_position, direction_vector))
    return (new_position)
   
   
def check(head, tail):
    diff = list(np.subtract(head, tail))
    if diff == [2,0] or diff == [-2,0] or diff == [0,2] or diff == [0,-2] or diff == [0,0]:
        diff = list(np.divide(diff, 2))
        tail = list(np.add(tail, diff))
        tail = list(np.array(tail).astype(int))
    elif abs(diff[0]) >= 2 or abs(diff[1]) >= 2:
        to_move = [math.copysign(1,diff[0]), math.copysign(1,diff[1])]
        to_move = list(np.array(to_move).astype(int))
        tail = move(tail, to_move)
    return(tail)

fp = open('data/day9-input.txt')
lines = fp.read().split('\n')

head_position = [0,0]
tail_position = [0,0]
rope_positions = [[0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0]]
tail_visited_part1 = []
tail_visited_part2 = []

for line in lines:
    head_movements = line.split(' ')
    for movement in range(0, int(head_movements[1])):
        head_position = move(head_position, calculate_direction(head_movements[0]))
        rope_positions[0] = move(rope_positions[0], calculate_direction(head_movements[0]))
        tail_position = check(head_position, tail_position)
        for i in range(0, len(rope_positions)-1):
            rope_positions[i+1] = check(rope_positions[i], rope_positions[i+1])       
        if tail_position not in tail_visited_part1:
            tail_visited_part1.append(tail_position)
        if rope_positions[-1] not in tail_visited_part2:
            tail_visited_part2.append(rope_positions[-1])

print('answer to part 1 -', len(tail_visited_part1))
print('answer to part 2 -', len(tail_visited_part2))