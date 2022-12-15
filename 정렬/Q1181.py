import sys


def user_input():
    return sys.stdin.readline()


testCases = ['but', 'i', 'wont', 'hesitate', 'no', 'more', 'no', 'more', 'it', 'cannot', 'wait', 'im', 'yours']
filterList = list(set(testCases))
filterList.sort()
print(filterList)
# testLen = int(user_input())
testLen = 13
# testCases = []
# for i in range(testLen):
#     testCases.append(user_input())
