userInput = input()
strMap = {"a":-1, "b":-1, "c":-1, "d":-1, "e":-1, "f":-1, "g":-1, "h":-1, "i":-1, "j":-1, "k":-1, "l":-1, "m":-1, "n":-1, "o":-1, "p":-1, "q":-1, "s":-1,
                "t":-1, "u":-1, "v":-1, "w":-1, "x":-1, "y":-1, "z":-1 }
for i in range(len(userInput)):
    strMap[userInput[i]] = i

for i in list(strMap.values()):
    print(i , end= " ")


# S = input()
# abc ='abcdefghijklmnopqrstuvwxyz'

# for i in abc:
#     if i in S:
#         print(S.index(i), end= ' ')
#     else:
#         print( -1, end =' ')