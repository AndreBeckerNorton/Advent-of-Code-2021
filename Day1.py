with open('Day1.txt') as f:
    depths2 = f.readlines()
'''
sumD = 0
currDepth = 0
prevDepth = 0

for depth in depths:
    currDepth = depth
    if currDepth > prevDepth:
        sumD += 1
    prevDepth = currDepth
'''
 # print(sumD)
 # Day one part one solved

sum3 = 0
currSum = 0
prevSum = 0
depthsClean = [int(i[:-1]) for i in depths2]
depthsSum = [sum(depthsClean[i:i+3]) for i in range(len(depthsClean))]
print(depthsSum)

for sum3 in depthsSum:
    currSum = sum3
    if currSum > prevSum:
        sum3 += 1
    prevDepth = currSum

print(sum3)


depths = [int(x) for x in open('Day1.txt').read().split('\n')]
print(sum([1 for i in range(len(depths)-1) if depths[i+1]>depths[i]])) #part 1
print(sum([1 for i in range(len(depths)-3) if depths[i+3]>depths[i]])) #part 2



