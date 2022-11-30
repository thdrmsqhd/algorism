testCaseCount = int(input())

# testCaseCount = int("2")
testCase = []
# testCase = ['3 ABC','5 /HTP']
for i in range(testCaseCount):
    testCase.append(input())

for i in testCase:
    iter = int(i.split()[0])
    str = i.split()[1]
    for j in str:
        print(j*iter, end= "")
    print()