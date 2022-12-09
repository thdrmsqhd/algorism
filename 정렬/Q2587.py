numList = []


def average(numbers):
    length = len(numbers)
    return sum(numbers) // length


for i in range(5):
    numList.append(int(input()))

print(average(numList))
numList.sort()
print(numList[2])