userInput = input()
# userInput = "Mississipi".lower()
# userInput = "z"
lowerStr = userInput.lower()
map = dict()
for i in lowerStr:
    if(map.get(i) == None):
        map[i] = 1
    else:
        map[i] = map[i] + 1
maxValue = 0
maxKey = ""
for i in map:
    if(map[i] >= maxValue):
        maxValue = map[i]
        maxKey = i
valueList = list(map.values())
valueList.sort()
if(len(valueList) > 1 and valueList[len(valueList)-1] == valueList[len(valueList)-2]):
    print("?")
else:
    print(maxKey.upper())