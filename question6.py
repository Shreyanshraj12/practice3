def singleNumber(nums):
    single = 0

    for num in nums:
        single ^= num

    return single
nums = [2, 2, 1]
result = singleNumber(nums)
print(result)  # Output: 1
