# Dongyoung Kwon @Chuncheonian (ehddud2468@gmail.com)

# 큰 정수 곱셈 Algorithm
def large_integer_prod(a: int, b: int) -> int:
    u, v = len(str(a)), len(str(b)) # 자릿수가 담긴 변수
    
    n =  max(u, v)

    # 예외 처리
    if (a == 0) or (b == 0):
        return 0
    
    # 일반적인 곱셈
    elif n <= 4: # Threshold -> 4
        return a * b
    
    # 재귀를 활용한 곱셈
    else:
        m = n // 2
        x, y = divmod(a, 10 ** m)
        w, z = divmod(b, 10 ** m)
        r = large_integer_prod(x + y, w + z)
        p = large_integer_prod(x, w)
        q = large_integer_prod(y, z)

        return p * (10 ** (2*m)) + (r - p - q) * (10 ** m) + q

# Testcase
a = 1_234_567_812_345_678
b = 2_345_678_923_456_789
print(large_integer_prod(a, b))
print(a*b)