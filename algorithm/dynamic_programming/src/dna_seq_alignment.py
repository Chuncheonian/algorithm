# Dongyoung Kwon @Chuncheonian (ehddud2468@gmail.com)
# python version requirement: >=3.9
# Minimum cost Sequence Alignment Algorithm

import utility  # 출력 관련 함수 모듈

a = ['A', 'A', 'C', 'A', 'G', 'T', 'A', 'C', 'C']
b = ['T', 'A', 'C', 'G', 'T', 'T', 'C', 'A']

m = len(a)
n = len(b)
dp = [[0 for _ in range(n+1)] for _ in range(m+1)]              # 마지막 행, 열에 '-' 틈 문자 추가된 (m+1 * n+1) 행렬 초기화
min_index = [[(0, 0) for _ in range(n+1)] for _ in range(m+1)]  # 최소비용 값인 원소를 어디로부터 구했는지를 담고 있는 행렬 초기화

for j in range(n-1, -1, -1):  # 마지막 행의 원소에 틈의 비용 추가
    dp[m][j] = dp[m][j+1] + 2

for i in range(m-1, -1, -1):  # 마지막 열의 원소에 틈의 비용 추가
    dp[i][n] = dp[i+1][n] + 2

# 최적 맞춤(점화식)을 만족하는 dp 생성
for i in range(m-1, -1, -1):  # i == row
    for j in range(n-1, -1, -1):  # j == col
        
        # 두 행렬의 첫번째 원소를 비교 (같으면 0, 다르면 1)
        penalty = 0
        if a[i] != b[j]:
            penalty = 1

        # 점화식: dp[i][j] = min(dp[i+1][j+1] + penalty, dp[i+1][j] + 2, dp[i][j+1] + 2)
        if dp[i+1][j+1] + penalty < dp[i+1][j] + 2:
            if dp[i+1][j+1] + penalty < dp[i][j+1] + 2:  # dp[i+1][j+1] + penalty가 가장 작은 경우
                dp[i][j] = dp[i+1][j+1] + penalty
                min_index[i][j] = (i+1, j+1)
            
            else:  # dp[i][j+1] + 2가 가장 작은 경우
                dp[i][j] = dp[i][j+1] + 2
                min_index[i][j] = (i, j+1)

        else:
            if dp[i+1][j] + 2 < dp[i][j+1] + 2:  # dp[i+1][j] + 2가 가장 작은 경우
                dp[i][j] = dp[i+1][j] + 2
                min_index[i][j] = (i+1, j)
            
            else:  # dp[i][j+1] + 2가 가장 작은 경우
                dp[i][j] = dp[i][j+1] + 2
                min_index[i][j] = (i, j+1)

# Testcase
utility.printMatrix(dp)
x = 0
y = 0

while x < m and y < n:
    tx, ty = x, y
    print(min_index[x][y])
    (x, y) = min_index[x][y]

    if x == tx + 1 and y == ty + 1:
        print(a[tx], ' ', b[ty])
    
    elif x == tx and y == ty + 1:
        print(' - ', ' ', b[ty])
    
    else:
        print(a[tx], ' ', ' -')