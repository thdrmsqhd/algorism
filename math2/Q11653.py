userInput = int(input())

i = 2
while userInput >= i:
    if userInput%i == 0:
        userInput = userInput // i
        print(i)
    else:
        i += 1