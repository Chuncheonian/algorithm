# Dongyoung Kwon @Chuncheonian (ehddud2468@gmail.com)
import utility  # 출력 관련 함수 모듈

class Node:
    def __init__(self, data: any):
        self.l_child: Node = None
        self.r_child: Node = None
        self.data = data

# Optimal-BST Algorithm: 평균 검색 시간이 제일 낮은, 가장 효율적인 BST를 찾는 탐색 알고리즘
def opt_search_tree(p: list[int]):
    # 가로축은 0 ~ n, 세로축은 1 ~ n+1
    n = len(p) - 1
    dp = [[0 for _ in range(n+2)] for _ in range(n+2)]  # dp[i][j] : min(dp[i][k-1] + dp[k+1][j]) + sum(p[i] ~ p[j]) (i <= k <= j, p[i]: i가 검색키일 확률)
    R = [[0 for _ in range(n+2)] for _ in range(n+2)]   # R[i][j] : i에서 j까지의 Node중 root인 Node의 번호

    # Initialize 2-D Matrix dp, R
    for i in range(1, n+1):
        dp[i][i-1] = 0      # 주 대각선 원소는 0
        dp[i][i] = p[i]     # 자기 자신 검색시간 = 1 * 자기 자신이 검색키일 확률
        R[i][i] = i         # 자기 자신의 트리의 루트는 자기 자신이다.
        R[i][i-1] = 0       # 주 대각선 원소는 0
    dp[n+1][n] = 0  # 주 대각선 원소중 마지막 원소를 0
    R[n+1][n] = 0   # 주 대각선 원소중 마지막 원소를 0

    for diagonal in range(1, n):  # 진행 순서가 주 대각선 기준에서 위로 올라간다.
        for i in range(1, n-diagonal+1):  # 기준 대각선에서 윗쪽 원소만 채움
            j = i + diagonal
            min_result = 99999  # 절대 될 수 없는 값으로 초기화
            min_k = 0           # k중 최소값을 가진 min_k 초기화

            # dp[i][k-1] + dp[k+1][j]의 최소값과 그 때의 k를 찾는 과정
            for k in range(i, j+1):  # i <= k <= j
                if (dp[i][k-1] + dp[k+1][j]) < min_result:
                    min_result = dp[i][k-1] + dp[k+1][j]
                    min_k = k

            dp[i][j] = min_result + sum(p[i : j+1]) # dp[i][j] = min(dp[i][k-1] + dp[k+1][j]) + sum(pi ~ pj)
            R[i][j] = min_k                         # R[i][j] = Root가 되는 Node의 번호    
    return dp, R

# R행렬을 이용해 Optimal-BST를 구축하는 Function
def tree(key: list[any], R: list[list[int]], i: int, j: int) -> Node:
    k = R[i][j]

    if k == 0:
        return
    else:
        p = Node(key[k])
        p.l_child = tree(key, R, i, k-1)
        p.r_child = tree(key, R, k+1, j)
        
        return p

# Testcase
key = [" ", "A", "B", "C", "D", "E"]
p = [0, 4/15, 5/15, 1/15, 3/15, 2/15]  # p[i] : key[i]가 검색키일 확률

dp, R = opt_search_tree(p)

utility.printMatrixF(dp) # print float Matrix
print()
utility.printMatrix(R)   # print int Matrix

root = tree(key, R, 1, 5)

utility.print_inOrder(root)
print()
utility.print_preOrder(root)