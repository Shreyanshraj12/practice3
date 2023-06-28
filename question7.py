def findMissingRanges(nums, lower, upper):
    result = []
    start = lower

    for num in nums:
        if num > start:
            if num - 1 == start:
                result.append(str(start))
            else:
                result.append(str(start) + "->" + str(num - 1))
        start = num + 1

    if start <= upper:
        if start == upper:
            result.append(str(start))
        else:
            result.append(str(start) + "->" + str(upper))

    return result
nums = [0, 1, 3, 50, 75]
lower = 0
upper = 99
result = findMissingRanges(nums, lower, upper)
print(result)  
