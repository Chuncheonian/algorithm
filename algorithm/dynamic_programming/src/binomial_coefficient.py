# Dongyoung Kwon @Chuncheonian (ehddud2468@gmail.com)
from numpy import *
import numpy as np
import time

# 이항계수의 두가지 접근 방법
class BinomialCoefficient:
    # Top-down, recursion
    def bin(self, n: int, k: int) -> int:
        if k == 0 or n == k:
            return 1
        else:
            return self.bin(n-1, k-1) + self.bin(n-1, k)

    # Bottom-Up, repeat
    def bin2(self, n: int, k: int) -> int:
        matrix = np.empty((n+1, n+1))
        for i in range(n+1):
            for j in range(min(i, k) + 1):
                if j == 0 or j == i:
                    matrix[i][j] = 1
                else:
                    matrix[i][j] = matrix[i-1][j-1] + matrix[i-1][j]
        return matrix[n][k]

# Testcase
bc = BinomialCoefficient()
print(bc.bin(10, 5))
print(bc.bin2(10, 5))

start = time.time()
result1 = bc.bin(20, 10)
end = time.time()
print("bin1 exec time in N=20 : ", end - start, ", result : ", result1)

start = time.time()
result2 = bc.bin2(1000, 500)
end = time.time()
print("bin2 exec time in N=1000 : ", end - start, ", result : ", result2)