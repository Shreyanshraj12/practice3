def nextPermutation(nums):
    i = len(nums) - 2
    while i >= 0 and nums[i] >= nums[i+1]:
        i -= 1

    if i >= 0:
        
        j = len(nums) - 1
        while j > i and nums[j] <= nums[i]:
            j -= 1

        
        nums[i], nums[j] = nums[j], nums[i]

    
    left = i + 1
    right = len(nums) - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
nums = [1, 2, 3]
nextPermutation(nums)
print(nums) 

nums = [2, 3, 1]
nextPermutation(nums)
print(nums)  

nums = [3, 2, 1]
nextPermutation(nums)
print(nums)  
