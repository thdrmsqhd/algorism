import sys

caseLen = int(input())
caseList = []

for i in range(caseLen):
    caseList.append(int(sys.stdin.readline()))


def average(pList: list) -> int:
    return round(sum(pList) / len(pList))


def midValue(pList: list) -> int:
    return pList[int(len(pList) // 2)]


def manyValue(pList: list) -> int:
    if len(pList) == 1:
        return pList[0]
    resultMap = dict()
    for i in pList:
        if resultMap.get(i) is None:
            resultMap[i] = 1
        else:
            resultMap[i] += 1
    maxValue = max(list(resultMap.values()))

    maxValueKeys = []
    for i in resultMap.keys():
        if resultMap[i] == maxValue:
            maxValueKeys.append(i)

    if len(maxValueKeys) != 1:
        maxValueKeys.sort()
        # return maxValueKeys[len(maxValueKeys)-1]
        # 두번째로 작은 값을 찾아야 한다.
        # 이미 정렬이 되어 있기 때문에 [1]번째 값이 두번째로 작은값
        return maxValueKeys[1]
    else:
        return maxValueKeys[0]


def minMaxRange(pList: list) -> int:
    numRange = []
    for i in range(pList[0], pList[len(pList) - 1]):
        numRange.append(i)
    return len(numRange)


caseList.sort()

print(average(caseList))
print(midValue(caseList))
print(manyValue(caseList))
print(minMaxRange(caseList))
