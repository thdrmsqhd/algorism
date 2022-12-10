caseLen = int(input())
testCase = []
for i in range(caseLen):
    testCase.append(list(map(int,input().split(" "))))

coordinate = [[0 for i in range(101)] for j in range(101)]
for case in testCase:
    x, y = case
    for i in range(x,x+10):
        for j in range(y,y+10):
            coordinate[i][j] = 1

answer = 0
for row in coordinate:
    answer += row.count(1)

print(answer)