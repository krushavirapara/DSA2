#Leetcode 

#1.Using hashmap
def majorityElement( nums) -> int:
    from collections import Counter
    c = Counter(nums)
    for i in c:
        if c[i]>=int(len(nums)/2):
            return i
        
print(majorityElement([3,2,3,2,1]))