# Dongyoung Kwon @Chuncheonian (ehddud2468@gmail.com)

# Merge Sort Algorithm: Divide-and-Conquer 접근법을 활용한 정렬 알고리즘
def merge_sort(n: int, arr: list[int]) -> None:
    if n <= 1:  # 예외 처리
        return
    
    h = n // 2  # h : 분할된 arr 배열의 왼쪽 배열의 길이
    m = n - h   # m : 분할된 arr 배열의 오른쪽 배열의 길이

    # arr 배열 분할
    l_arr = arr[:h]
    r_arr = arr[h:]

    merge_sort(h, l_arr)            # divide
    merge_sort(m, r_arr)            # divide
    merge(h, m, l_arr, r_arr, arr)  # combine
    
# 분할된 배열을 Conquer & Combine
def merge(h: int, m: int, l_arr: list[int], r_arr: list[int], arr: list[int]) -> None:
    i = 0   # i : 왼쪽 배열의 인덱스
    j = 0   # j : 오른쪽 배열의 인덱스
    k = 0   # k : merge될 배열의 인덱스

    while i < h and j < m:
        if l_arr[i] < r_arr[j]:
            arr[k] = l_arr[i]
            i += 1  # i를 증가함으로서 다음번에 왼쪽 배열의 다음 원소에 접근
        else:
            arr[k] = r_arr[j]
            j += 1  # j를 증가함으로서 다음번에 오른쪽 배열의 다음 원소에 접근
        k += 1  # k를 증가함으로서 다음번에 merge될 배열의 다음 원소에 접근

    if i >= h:  # 왼쪽 배열의 원소들보다 값이 큰 오른쪽 배열의 원소들을 merge될 배열에 삽입
        arr[k:h+m] = r_arr[j:m]
    else:       # 오른쪽 배열의 원소들보다 값이 큰 왼쪽 배열의 원소들을 merge될 배열에 삽입
        arr[k:h+m] = l_arr[i:h]

# Testcase
arr = [3,16,13,1,9,2,7,5,8,4,11,6,15,14,10,12]
merge_sort(len(arr), arr)
print(arr)