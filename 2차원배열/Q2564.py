# 구간이 겹쳤을 경우 - 를 하는 문제
# 구간이 겹치지 않으면 면적은 100
# 10에서 빠진 구간 만큼의 넓이를 빼준다
# 3
# x:3  y:7 
# x:15 y:7 
# x:5  y:2 
# 각각의 구간을 가지고있는다
# 구간들이 겹치는지 검증
# 겹친다면 얼마나 겹치는지
# 전체 종의 면적 - 겹치는 부분

# caseLen = int(input())
# colorPapers = []
# for i in range(len(caseLen)):
#     position = list(map(int,input().split(" ")))
#     square = \
# [position[0],position[0]+10],[position[1],position[1]+10]]
#     colorPapers.append(square)

colorPapers = [
    [[3,13],[7,17]],
    [[15,25],[7,17]],
    [[5,15],[2,12]]
]

for i in range(len(colorPapers)):
    for j in range(1, len(colorPapers)-1):
        print(colorPapers[i][0],colorPapers[j][0], end="/")
        print(colorPapers[i][1],colorPapers[j][1])
    print()