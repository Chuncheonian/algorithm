# Dongyoung Kwon @Chuncheonian (ehddud2468@gmail.com)

# Quick Sort Algorithm
def quick_sort(arr: list[int], low: int, high: int) -> None:
    def partition(arr: list[int], low: int, high: int) -> int:
        pivot = arr[low]    # 배열의 첫번째 원소를 pivot으로 선정
        j = low             # j : pivot보다 작은 원소중 가장 큰 인덱스

        for i in range(low + 1, high + 1): # 배열의 나머지 원소들을 pivot이랑 비교
            if arr[i] < pivot:
                j += 1
                arr[i], arr[j] = arr[j], arr[i]
        pivot_point = j
        arr[low], arr[pivot_point] = arr[pivot_point], arr[low] # 

        return pivot_point

    if low < high:
        pivot_point = partition(arr, low, high)
        quick_sort(arr, low, pivot_point - 1)   
        quick_sort(arr, pivot_point+1, high)

# Testcase
arr = [3,5,2,9,10,14,4,8]
quick_sort(arr, 0, len(arr)-1)
print(arr)