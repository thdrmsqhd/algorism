# userInput = input()
userInput = "ddz=z="
reTarget = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
for i in reTarget:
    print(i)
    userInput = userInput.replace(i ,str(1))
    print(userInput)
    print("----------------")


print(len(userInput))