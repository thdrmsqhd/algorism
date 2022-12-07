numArr = []
for i in range(9):
    numArr.append(list(map(int,input().split(" "))))

resultMap = dict(maxNumber = 0, y = 0, x = 0)
for i in range(len(numArr)):
    if max(numArr[i]) >= resultMap["maxNumber"]:
        resultMap["maxNumber"] = max(numArr[i])
        resultMap["y"] = i + 1
        resultMap["x"] = numArr[i].index(max(numArr[i])) + 1

print(resultMap["maxNumber"])
print(resultMap["y"], resultMap["x"])