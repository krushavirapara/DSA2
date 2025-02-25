#brute force would be to sort array and then find longest length O(nlogn)


#optimal O(n)
#using hashtable
def longest_consecutive_sequence(nums):
    hash  = set(nums)
    longest = 0
    for i in range(len(nums)):
        length=0
        while nums[i]+length in hash:
            length+=1
        longest =  max(length,longest)
    return longest

print(longest_consecutive_sequence([100,4,1,2,200,3]))

   