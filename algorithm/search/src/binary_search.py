# Dongyoung Kwon @Chuncheonian (ehddud2468@gmail.com)
# python version requirement: >=3.9

def binary_search(nums: list[int], target: int) -> int:
    lhs = 0
    rhs = len(nums) - 1

    while lhs <= rhs:
        mid = lhs + (rhs - lhs) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            lhs = mid + 1
        else:
            rhs = mid - 1
    
    return -1

# Testcase
print(binary_search([1,2,3,4,5], 4))  # > 3