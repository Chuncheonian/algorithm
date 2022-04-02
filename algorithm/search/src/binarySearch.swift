// Dongyoung Kwon @Chuncheonian (ehddud2468@gmail.com)

func binarySearch(nums: [Int], target: Int) -> Int {
    var (lhs, rhs) = (0, nums.count - 1)
        
    while lhs <= rhs {
        let mid = lhs + (rhs - lhs) / 2
            
        if nums[mid] == target {
            return mid
        }
        nums[mid] > target ? (rhs = mid - 1) : (lhs = mid + 1)
    }
    return -1
}

// Testcase
print(binarySearch(nums: [1, 2, 3, 4, 5], target: 4))  // > 3