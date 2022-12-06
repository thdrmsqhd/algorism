# 3 3
# 1 1 1
# 2 2 2
# 0 1 0
# 3 3 3
# 4 4 4
# 5 5 100

x, y = list(map(int, input().split(" ")))


def make_metrix(width, height):
    matrix = []
    for _ in range(height):
        matrix.append(list(map(int,input().split(" "))))
    return matrix


matrix_arr = [
                [
                    [1,1,1],
                    [2,2,2],
                    [0,1,0]
                ],
                [
                    [3,3,3],
                    [4,4,4],
                    [5,5,100]
                ]
            ]
for i in range(2):
    matrix_arr.append(make_metrix(x, y))

print(matrix_arr[0][0][0])
print(matrix_arr[1][0][0])
