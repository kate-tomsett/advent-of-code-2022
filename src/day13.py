import operator

def compare_vals(left, right):
    type_left = type(left)
    type_right = type(right)
    print(left, type_left, right, type_right)
    if type_left == type_right:
        if type_left is int:
            if left > right:
                #print('left bigger than right so false')
                return False
            elif left < right:
                #print('left is smaller than right so true')
                return True
            else:
                #print('they are equal')
                return 'Continue'
        elif type_left is list:
            if len(left) <= len(right):
                for (sub_val_left, sub_val_right) in zip(left, right):
                    ordered = compare_vals(sub_val_left, sub_val_right)
                    if ordered != 'Continue':
                        return ordered
                        #print('had a problem comparing two lists ,false')
            else:
                #print('right has fewer elements than left so false')
                return False
    else:
        if type_left is int:
            if right == []:
                return False
            else:
                return compare_vals(left, right[0])
        elif type_right is int:
            if left == []:
                return True
            else:
                return compare_vals(left[0], right)
    
    return 'Continue'



fp = open('day13-input.txt')

input = fp.read().split('\n')
new_input = []

while ('' in input):
    input.remove('')
for line in input:
    new_input.append(eval(line))

sum = 0

for i in range(0, len(new_input), 2):
    ordered = True

    packet_left = new_input[i]
    packet_right = new_input[i+1]
    
    print(i, len(packet_left), len(packet_right))
    if len(packet_left) <= len(packet_right):
        for value in range(0, len(packet_left)):
            val_left = packet_left[value]
            val_right = packet_right[value]
            ordered = compare_vals(val_left, val_right)
            if ordered == False:
                #print('that value returned false')
                break
            elif ordered == True:
                #print('that value returned true')
                break
            
            if value == len(packet_left)-1:
                #print('made it to end of left')
                ordered = True
                break
    else:
        #print('right has fewer elements than left so false')
        ordered = False

    if ordered:
        sum += int((i/2) + 1)
        
        
        
print('Answer to part 1 -', sum)