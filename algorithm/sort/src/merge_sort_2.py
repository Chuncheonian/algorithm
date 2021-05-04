# Dongyoung Kwon @Chuncheonian (ehddud2468@gmail.com)

# Merge Sort 2 : 공간복잡도가 향상된 MergeSort 알고리즘
def merge_sort2(arr: list[int], low: int, high: int) -> None:
    if low >= high: # 예외 처리
        return
    
    mid = (low + high) // 2

    merge_sort2(arr, low, mid)      # divide
    merge_sort2(arr, mid+1, high)   # divide
    merge2(arr, low, mid, high)     # combine

# 분할된 배열을 Conquer & Combine
def merge2(arr: list[int], low: int, mid: int, high: int) -> None:
    i = low
    j = mid + 1
    k = 0
    tmp_arr = [0] * (high - low + 1)

    while (i <= mid) and (j <= high):
        if arr[i] < arr[j]:
            tmp_arr[k] = arr[i]
            i += 1
        else:
            tmp_arr[k] = arr[j]
            j += 1
        k += 1

    if i > mid:
        for idx in range(j, high + 1):
            tmp_arr[k - j + idx] = arr[idx]
    else:
        for idx in range(i, mid + 1):
            tmp_arr[k - i + idx] = arr[idx]
    
    for idx in range(low, high + 1): # 복사
        arr[idx] = tmp_arr[idx - low]

# Testcase
arr = [3,16,13,1,9,2,7,5,8,4,11,6,15,14,10,12]
merge_sort2(arr, 0, len(arr)-1)
print(arr)