import sys

caseLen = sys.stdin.readline()
testCases = list(map(int,sys.stdin.readline().split(" ")))

setCases = list(set(testCases))
setCases.sort()
countMap = dict()
for i in range(len(setCases)):
    countMap[setCases[i]] = i


for i in testCases:
    print(countMap[i], end=" ")
