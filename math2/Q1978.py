# length = int(input())
# userInput = list(map(int,input()))
# 1은 소수가 아니

# 배열을 먼저 만든다.
# 배열에서 i*2를 모두 0으로 바꾼다
# 0이 아닌것들은 모두 소수이다
arr = []
for i in range(0,101):
    arr.append(i)
# print(arr)
# print(len(arr))
for i in range(2,11):
    for j in range(2, 11):
        arr[i*j] = 0

for i in arr:
    if i != 0:
        print(i)