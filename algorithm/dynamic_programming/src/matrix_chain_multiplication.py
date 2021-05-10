# Dongyoung Kwon @Chuncheonian (ehddud2468@gmail.com)
import utility

def matrix_chain_multiplication(d: list[int]):
    n = len(d) - 1
    dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
    P = [[0 for _ in range(n+1)] for _ in range(n+1)]   # P[i][j] : 최적 순서를 얻기 위해 최소값을 주는 k값을 담는 행렬

    for i in range(n):
        dp[i][i] = 0  # 점화식
    
    for diagonal in range(1, n):
        for i in range(1, n - diagonal + 1):
            j = i + diagonal    # 진행방향이 대각선
            min_result = 99999  # 절대 될 수 없는 값으로 초기화
            min_k = 0

            # k에 따른 점화식의 최소값 찾기
            for k in range(i, j):  # i <= k <= j-1
                tmp_result = dp[i][k] + dp[k+1][j] + d[i-1] * d[k] * d[j]  # 점화식
                if tmp_result < min_result:
                    min_result = tmp_result
                    min_k = k

            dp[i][j] = min_result
            P[i][j] = min_k
    return dp, P

def order(P: list[list[int]], i: int, j: int):
    if i == j:
        print("A" + str(i), end='')
    else:
        k = P[i][j]
        print("(", end='')
        order(P, i, k)
        order(P, k+1, j)
        print(")", end='')

# Testcase
d = [5, 2, 3, 4, 6, 7, 8]  # 5*2, 2*3, 3*4, 4*6. 6*7, 7*8
dp, P = matrix_chain_multiplication(d)
utility.printMatrix(dp)
print()
utility.printMatrix(P)
order(P, 1, 6)
