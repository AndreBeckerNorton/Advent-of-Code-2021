with open('Day3.txt') as f:
    nums = f.read().splitlines()
num0 = 0
num1 = 0
num2 = 0
num3 = 0
num4 = 0
num5 = 0
num6 = 0
num7 = 0
num8 = 0
num9 = 0
num10 = 0
num11 = 0
for num in nums:
    for i in range(len(num)):
        if i == 0:
            num0 += int(num[i])
        if i == 1:
            num1 += int(num[i])
        if i == 2:
            num2 += int(num[i])
        if i == 3:
            num3 += int(num[i])
        if i == 4:
            num4 += int(num[i])
        if i == 5:
            num5 += int(num[i])
        if i == 6:
            num6 += int(num[i])
        if i == 7:
            num7 += int(num[i])
        if i == 8:
            num8 += int(num[i])
        if i == 9:
            num9 += int(num[i])
        if i == 10:
            num10 += int(num[i])
        if i == 11:
            num11 += int(num[i])

numList = [num0, num1, num2, num3, num4, num5, num6, num7, num8, num9, num10, num11]
numStr = ''
for num in numList:
    if num < 500:
        numStr += '0'
    else:
        numStr += '1'


print(1529 * 2566)
# brute force ^

from collections import Counter

ll = [x for x in open('Day3.txt').read().strip().split('\n')]

theta = ''
epsilon = ''
for i in range(len(ll[0])):
    common = Counter([x[i] for x in ll])

    if common['0'] > common['1']:
        ll = [x for x in ll if x[i] == '0']
    else:
        ll = [x for x in ll if x[i] == '1']
    theta = ll[0]

ll = [x for x in open('Day3.txt').read().strip().split('\n')]
for i in range(len(ll[0])):
    common = Counter([x[i] for x in ll])

    if common['0'] > common['1']:
        ll = [x for x in ll if x[i] == '1']
    else:
        ll = [x for x in ll if x[i] == '0']
    if ll:
        epsilon = ll[0]
print(int(theta,2)*int(epsilon,2))