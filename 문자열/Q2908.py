userInput = list(input().split())
userInput[0] = userInput[0][::-1]
userInput[1] = userInput[1][::-1]
userInput.sort()
print(userInput[1])