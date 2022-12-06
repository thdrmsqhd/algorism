import math


def isPrime(start, end):
    # 에라스토 테네스의 체
    if end == 1:
        return 1
    numList = [True for i in range(end + 1)]
    numList[0] = numList[1] = False
    target = int(math.sqrt(end))
    for i in range(2, target + 1):
        for j in range(i * i, end + 1, i):
            numList[j] = False
    count = 0
    for i in range(len(numList)):
        if numList[i] == True and i > start:
            count += 1
    return count


while True:
    start = int(input())
    if start == 0:
        break

    end = start * 2

    print(isPrime(start, end))
