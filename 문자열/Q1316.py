userInput = input()
testCases = []

for i in range(0, int(userInput)):
    testCases.append(input())

groupCount = 0

for case in testCases:
    map = dict()
    list = []
    for i in range(len(case)):
        if(map.get(case[i]) != None):
            _list = []
            _list = map.get(case[i])
            _list.append(i)
            map[case[i]] = _list
        else:
            list.append(i)
            map[case[i]] = list
            list = []

    check = True
    for i in map.values():
        if(len(i) != 1):
            for j in range(len(i)-1):
                bigger = i [j+1]
                smaller = i [j]
                result = bigger - smaller
                if(result > 1):
                    check = False

    if(check):
        groupCount += 1

print(groupCount)
