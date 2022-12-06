targetLen = int(input())
testCases = []
for i in range(targetLen):
    testCases.append(int(input()))

primeList = [True for i in range(10000+1)]
primeList[0] = primeList[1] = False
rootLen = int(10000**0.5)

for i in range(2, rootLen+1):
    for j in range(i*i, 10000+1, i):
        primeList[j] = False

for i in testCases:
    forward = i//2
    backward = i//2
    while forward>0:
        if primeList[forward] and primeList[backward]:
            print(forward, backward)
            break
        forward -= 1
        backward += 1
