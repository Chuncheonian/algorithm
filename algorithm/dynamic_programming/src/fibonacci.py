# Dongyoung Kwon @Chuncheonian (ehddud2468@gmail.com)
import collections

# 1. fibonacci-bruteforce
def fib_bruteforce(n: int) -> int:
    if n <= 1:
        return n

    return fib_bruteforce(n-1) + fib_bruteforce(n-2)

# 2. fibonacci-memoization: Top-Down
dp = collections.defaultdict(int)

def fib_memoization(n: int) -> int:
    if n <= 1:
        return n

    if dp[n] == True:
        return dp[n]

    dp[n] = fib_memoization(n-1) + fib_memoization(n-2)
    
    return dp[n]
    
# 3. fibonacci-tabulation: Bottom-Up
dp2 = collections.defaultdict(int)

def fib_tabulation(n: int) -> int:
    dp2[1] = 1

    for i in range(2, n + 1):
        dp2[i] = dp2[i - 1] + dp2[i - 2]

    return dp2[n]

# 4. Space complexity improved fibonacci
def fib_simple(n: int) -> int:
    x, y = 0, 1

    for _ in range(n):
        x, y = y, x + y

    return x

# Testcase
print(fib_bruteforce(5))
print(fib_memoization(5))
print(fib_tabulation(5))
print(fib_simple(5))