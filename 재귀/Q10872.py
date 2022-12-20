def factorial(param):
    result = 0
    if param == 0 or param == 1:
        return 1
    if param != 1:
        result = param * factorial(param - 1)
    return result


num = int(input())
print(factorial(num))
