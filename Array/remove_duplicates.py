def remove_duplicates(nums):
    new_nums = []
    for i in range(len(nums)):
        if nums[i] not in new_nums:
            new_nums.append(nums[i])
    return len(new_nums)

print(remove_duplicates([1,12,21,1,12]))