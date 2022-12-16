import sys
caseLen = int(sys.stdin.readline())
testCases = []
for i in range(caseLen):
    userInput = sys.stdin.readline().split(' ')
    innerList = [i, int(userInput[0]), userInput[1]]
    testCases.append(innerList)


testCases.sort(key=lambda x: (x[1], x[0]))
for i in testCases:
    print(i[1], i[2], end="")
