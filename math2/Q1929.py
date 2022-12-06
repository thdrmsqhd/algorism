start, end = map(int, input().split())

numList = [True for i in range(end+1)]
max = int((end + 1) ** 0.5)

for i in range(2, max + 1):
    if numList[i] == True:
        for j in range(i*i, end + 1, i):
            numList[j] = False

solve = [i for i in range(2, end + 1) if numList[i] == True]

for i in range(len(solve)):
    if solve[i] >= start:
        print(solve[i])