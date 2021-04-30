# Dongyoung Kwon @Chuncheonian (ehddud2468@gmail.com)
import copy

# Floyd-Warshall Algorithm: 모든 정점에서 모든 정점까지의 최단 경로
def floyd_warshall(g: list[list[int]], n: int) -> list[list[int]]:
    dist = copy.deepcopy(g)  # dist: 최단 경로의 길이를 담은 행렬

    for k in range(0, n):  # 거치는 점
        for i in range(0, n):  # 시작점
            for j in range(0, n):  # 끝점
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist

# Floyd-Warshall 알고리즘을 통한 최단 경로를 구성하는 정점 기록
def floyd_warshall_2(g: list[list[int]], n: int):
    dist = copy.deepcopy(g)
    p = [[0] * n for _ in range(n)]  # p: 중간에 정점이 없으면 0, 있으면 그 중 가장 큰 인덱스를 포함한 행렬

    for k in range(0, n):
        for i in range(0, n):
            for j in range(0, n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    p[i][j] = k + 1  # 경로 중 가장 큰 인덱스 저장
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist, p

# print 2-D Matrix
def printMatrix(d: list[list[int]]) -> None:
    n = len(d[0])
    
    for i in range(0, n):
        for j in range(0, n):
            print(d[i][j], end=' ')
        print()

# 특정 두 정점 사이의 최단 경로 출력
def printPath(p: list[list[int]], q: int, r: int) -> None:
    if p[q-1][r-1] != 0:  # 최단 경로가 경유지를 지날 경우
        printPath(p, q, p[q-1][r-1])  # 시작 정점에서 경유하는 정점까지의 경로 검사
        print(f'v{p[q-1][r-1]}', end=' ')
        printPath(p, p[q-1][r-1], r)  # 경유하는 정점에서 끝 정점까지의 경로 검사

# Testcase
INF = 1000
# g = [ [0, 1, INF, 1, 5],
#       [9, 0, 3, 2, INF],
#       [INF, INF, 0, 4, INF],
#       [INF, INF, 2, 0, 3],
#       [3, INF, INF, INF, 0] ]
g = [ [0, 1, INF, INF, 3, INF, INF],
      [INF, 0, 4, 1, 3, INF, INF],
      [INF, INF, 0, INF, INF, INF, 1],
      [INF, INF, 1, 0, INF, 3, INF],
      [INF, INF, INF, 2, 0, 1, INF],
      [INF, INF, INF, INF, INF, 0, 2],
      [INF, INF, INF, INF, INF, INF, 0]]


d, p = floyd_warshall_2(g, 7)
print()
printMatrix(d)
print()
printMatrix(p)
print()
printPath(p, 1, 3)