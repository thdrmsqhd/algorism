import sys


def recursion(s, l, r, count):
    count += 1
    if l >= r:
        return 1, count
    elif s[l] != s[r]:
        return 0, count
    else:
        return recursion(s, l + 1, r - 1, count)


def isPalindrome(s, count):
    return recursion(s, 0, len(s) - 1, count)


caseLen = int(sys.stdin.readline())
# caseLen = 5
# testCase = ["AAA", "ABBA", "ABABA", "ABCA", "PALINDROME"]
testCase = []
for i in range(caseLen):
    testCase.append(input())
for i in testCase:
    j, k = isPalindrome(i, 0)
    print(j, k)
