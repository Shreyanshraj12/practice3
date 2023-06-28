def searchInsert(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left
nums = [1, 3, 5, 6]
target = 5
print(searchInsert(nums, target))  

nums = [1, 3, 5, 6]
target = 2
print(searchInsert(nums, target))  

nums = [1, 3, 5, 6]
target = 7
print(searchInsert(nums, target))  

nums = [1, 3, 5, 6]
target = 0
print(searchInsert(nums, target))  