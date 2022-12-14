import math

class Monkey:

    def __init__ (self, name, holding, operation, test_divisible_by, if_true, if_false):
        self.name = name
        self.holding = holding
        self.operation = operation
        self.test_divisible_by = test_divisible_by
        self.if_true = if_true
        self.if_false = if_false
        self.num_inspected = 0

fp = open('day11-input.txt')

inputs = fp.read().split('\n')

while ('' in inputs):
    inputs.remove('')

for input in inputs:
    inputs[inputs.index(input)] = input.lstrip()

name = 0
holding = []
monkeys = []
monkeys_inspected = []
mod = 1

for i in range(0, len(inputs)):
    line = inputs[i].split(' ')
    if line[0] == 'Monkey':
        name = line[1].split(':')[0]
        line = inputs[i+1]
        if 'Starting items: ' in line:
            holding = line[16:len(line)].split(',')
            for item in range(0, len(holding)):
                holding[item] = int(holding[item].lstrip())
        line = inputs[i+2]
        if 'Operation: new = ' in line:
            operation = line[17:len(line)]
        line = inputs[i+3]
        if 'Test: divisible by ' in line:
            test_divisible_by = int(line[18:len(line)])
            mod *= test_divisible_by
        line = inputs[i+4]
        if 'If true: throw to monkey ' in line:
            if_true = int(line[25:len(line)])
        line = inputs[i+5]
        if 'If false: throw to monkey ' in line:
            if_false = int(line[26:len(line)])
        monkeys.append(Monkey(name, holding, operation, test_divisible_by, if_true, if_false))
    
for round in range(0, 10000):
    for monkey in monkeys:
        for item in monkey.holding:
            monkey.num_inspected += 1
            old = item
            operation = monkey.operation
            new = eval(operation)
            num_divide_by = monkey.test_divisible_by
            new = new%mod
            if (new%num_divide_by == 0):
                monkeys[monkey.if_true].holding.append(new)
            else:
                monkeys[monkey.if_false].holding.append(new)
        monkey.holding = []

for monkey in monkeys:
    monkeys_inspected.append(monkey.num_inspected)

monkeys_inspected.sort()
monkeys_inspected.reverse()
monkey_business = monkeys_inspected[0] * monkeys_inspected[1]

print('Answer to part 2 =', monkey_business)