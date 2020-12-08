def accumulate(instructions):
    pos = accumulator = 0
    order = 1
    visited = dict()
    while pos not in visited.keys():
        visited[pos] = order
        inst = instructions[pos]
        if inst[0] == 'acc':
            accumulator += inst[1]
            pos += 1
        elif inst[0] == 'jmp':
            pos += inst[1]
        else:
            pos += 1
        if pos == len(instructions):
            return accumulator
    return False

def possible_instructions(instructions, jmp_locs, nop_locs):
    yield instructions
    for jmp_loc in jmp_locs:
        tmp_instructions = [i.copy() for i in instructions]
        tmp_instructions[jmp_loc][0] = 'nop'
        yield tmp_instructions
    for nop_loc in nop_locs:
        tmp_instructions = [i.copy() for i in instructions]
        tmp_instructions[nop_loc][0] = 'jmp'
        yield tmp_instructions

instructions = list()
jmp_locs = set()
nop_locs = set()

with open('input.txt', 'r') as f:
    for i, line in enumerate(f):
        instruction, value = line.strip().split(' ')
        instructions.append([instruction, int(value)])
        if instruction == 'nop':
            nop_locs.add(i)
        if instruction == 'jmp':
            jmp_locs.add(i)

possibilities = possible_instructions(instructions, jmp_locs, nop_locs)
acc = False
while not acc:
    variant = next(possibilities)
    acc = accumulate(variant)
print(acc)
