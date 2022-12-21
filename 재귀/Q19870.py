def fibonacci(num):
    result = 0
    if num == 0:
        return 0
    else:
        result = num + fibonacci(num-1)
        return result


# testNumber = int(input())
testNumber = 17
print(fibonacci(testNumber))