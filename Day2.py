with open('Day2.txt') as f:
    commands = f.read().splitlines()

hPos = 0
vPos = 0
aim = 0

for command in commands:
    cNum = int(command[-1])
    if 'forward' in command:
        hPos += cNum
        vPos += aim * cNum
    if 'up' in command:
        aim -= cNum
    if 'down' in command:
        aim += cNum

print(hPos * vPos)