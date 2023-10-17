def find_missing_number(nums):
    r = len(nums) + 1
    for i in range(r):
        if i not in nums:
            return i

print(find_missing_number([0,1]))