import sys


testLen = int(sys.stdin.readline())
testCases = set()
for i in range(testLen):
    testCases.add(sys.stdin.readline())

valueLenList = []
for element in testCases:
    valueList = [element, len(element)]
    valueLenList.append(valueList)

valueLenList.sort(key=lambda x: (x[1], x[0]))
for valueLen in valueLenList:
    print(valueLen[0], end="")