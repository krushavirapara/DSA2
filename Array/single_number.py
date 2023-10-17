def singleNumber(nums) -> int:
    hash_map = {}
    for i in nums:
        if i in hash_map:
            hash_map[i] += 1
        else:
            hash_map[i] = 1
    for i in hash_map:
        if hash_map[i] == 1:
            return i

print(singleNumber([1,2,2,1,3]))