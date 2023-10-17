from typing import List

#leetcode 1
#brute force 
def twoSum(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            temp = nums[i]+nums[j]
            if temp == target:
                return [i,j]

#better
def twoSum( nums: List[int], target: int) -> List[int]:
    m = {}
    for i in range(len(nums)):
        if target-nums[i] in m:
            return [m[target-nums[i]],i]
        m[nums[i]]=i       

print(twoSum([3,2,3],6))