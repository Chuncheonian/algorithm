# Merge Sort (합병 정렬)

> 분할 정복 접근법을 활용한 정렬 알고리즘

<br>

## 아이디어
* 합병 정렬은 **재귀 용법**을 활용한 정렬 알고리즘으로, 전체 원소를 가장 작은 단위로 분할한 후 분할한 원소를 다시 병합하는 정렬 방식이다.

<br>

## 알고리즘 설계 및 구현

<p align="center">
  <img src = "./img/merge_sort_1.gif" width="40%" alt="1">
</p>  

1. **예외처리**
 - 리스트의 길이가 1 이하이면 이미 정렬된 것으로 판단하여 종료. 그렇지 않은 경우에는,

2. **분할(Divide)**
  - 정렬되지 않은 리스트를 절반으로 잘라 비슷한 크기의 두 부분 리스트로 나눈다.

3. **정복(Conquer)**
  - 각 부분 리스트를 재귀적으로 합병 정렬을 이용해 정렬한다.

4. **조합(Combine)**
  - 두 부분 리스트를 다시 하나의 정렬된 리스트로 합병한다.

<br>

## 시간 복잡도

최선과 최악 모두 `O(nlogn)` 이며, `안정 정렬`이다.

|   평균   |   최선   |   최악   |
| :------: | :------: | :------: |
| O(nlogn) | O(nlogn)	| O(nlogn) |

<br>

> [시간복잡도 구하는 방법](https://devlimk1.tistory.com/138)

<br>

## Source Code
``` python
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
```

<br>

## 공간 복잡도가 향상된 Source Code
``` python
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
```