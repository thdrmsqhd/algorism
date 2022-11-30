outArr = []
for i in range(0,15):
    inArr = []
    for j in range(0,15):
        inArr.append(0)
    outArr.append(inArr)

for i in range(0,15):
    for j in range(0,15):
        inArr = []
        if i == 0:
            outArr[i][j] = j+1
        else:
            if j == 0:
                outArr[i][j] = outArr[i-1][j]
            else:
                outArr[i][j] = outArr[i][j-1] + outArr[i-1][j]

def countPerson(x, y):
    print(outArr[x][y-1])


inputLen = int(input())
testCases = []
for i in range(0, inputLen):
    arr = []
    arr.append(input())
    arr.append(input())
    testCases.append(arr)

for case in testCases:
    case = list(map(int, case))
    countPerson(case[0], case[1])