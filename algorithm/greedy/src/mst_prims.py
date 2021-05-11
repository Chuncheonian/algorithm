# Dongyoung Kwon @Chuncheonian (ehddud2468@gmail.com)
import utility

def prim(W: list[list[int]]) -> set:
    F = set()           # F : Solution set
    n = len(W)          # n : vertex 갯수
    nearest = [0] * n   # nearest:  Solution set에 속한 vertex중에서 vi에서 가장 가까운 vertex의 인덱스
    distance = [0] * n  # distance: vi와 nearest[i]를 잇는 edge' weight

    for i in range(1, n):
        nearest[i] = 0
        distance[i] = W[0][i]  # vi와 v0을 잇는 edge' weight로 초기화
    print(nearest)
    print(distance)

    # n-1개의 vertex를 조사
    for _ in range(1, n):
        min_weight = INF    # 될 수 없는 값으로 초기화
        vertex_near = 0     # vertex_near : Solution set에 속하지 않으면서 weight가 가장 작은 vertex
        
        # 시작 vertex를 제외한 모든 vertex 조사
        for i in range(1, n):
            if 0 <= distance[i] < min_weight:  # weight가 가장 작은 vertex를 찾으면
                min_weight = distance[i]
                vertex_near = i

        F.add((vertex_near, nearest[vertex_near]))  # 가장 작은 weight를 가진 edge간의 두 vertex 저장
        distance[vertex_near] = -1                  # 방금 찾은 vertex 다시 검사되는 것을 방지

        for i in range(1, n):
            if W[i][vertex_near] < distance[i]:  # 방금 찾은 vertex에서 다른 vertex간의 weight를 update
                distance[i] = W[i][vertex_near] 
                nearest[i] = vertex_near
    return F

# Testcase
INF = 1000
# W[i][j] = edge' weight  -> vi, vj 사이의 edge가 있는 경우
# W[i][j] = INF           -> vi, vj 사이의 edge가 없는 경우
# W[i][j] = 0             -> i == j
W = [[0, 1, 3, INF, INF],
     [1, 0, 3, 6, INF],
     [3, 3, 0, 4, 2],
     [INF, 6, 4, 0, 5],
     [INF, INF, 2, 5, 0]]

utility.printMatrix(W)
print()
print(prim(W))