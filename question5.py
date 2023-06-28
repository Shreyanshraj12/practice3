def plusOne(digits):
    carry = 1

    for i in range(len(digits) - 1, -1, -1):
        digits[i] += carry
        carry = digits[i] // 10
        digits[i] %= 10

    if carry == 1:
        digits.insert(0, 1)

    return digits
digits = [1, 2, 3]
result = plusOne(digits)
print(result) 
