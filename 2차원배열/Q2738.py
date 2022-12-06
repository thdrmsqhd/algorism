x, y = list(map(int, input().split(" ")))


def make_metrix(height):
    matrix = []
    for _ in range(height):
        matrix.append(list(map(int,input().split(" "))))
        
    return matrix


matrix_arr = []
matrix_arr.append(make_metrix(x))
matrix_arr.append(make_metrix(x))

for i in range(x):
    for j in range(y):
        print(matrix_arr[0][i][j] + matrix_arr[1][i][j], end= " ")
    print()