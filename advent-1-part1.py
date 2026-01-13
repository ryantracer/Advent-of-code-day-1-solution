count = 0
pos = 50

def cycle(value, change, op):
    if op == 'R':
        return (value + change) % 100
    elif op == 'L':
        return (value - change) % 100

with open('input.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        s = line
        letter = s[0]
        num = int(s[1:])
        print(cycle(pos, num, letter))
        pos = cycle(pos, num, letter)
        if pos == 0:
            count += 1

print(f'Password: {count}')
