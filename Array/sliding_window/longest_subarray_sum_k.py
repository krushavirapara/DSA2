


# #1.brute force
# def longest_subarray_sum_k(nums,k):
#     max_len = 0
#     for i in range(len(nums)):
#         for j in range(i,len(nums)):
#             s=0
#             for z in range(i,j+1):
#                 s+=nums[z]
#             if s==k:
#                 max_len = max(max_len,j-i+1)
#     return max_len

# #2optimized brute force
# def longest_subarray_sum_k(nums,k):
#     max_len = 0
#     for i in range(len(nums)):
#         s=0
#         for j in range(i,len(nums)):
#             s+=nums[j]
#             if s==k:
#                 max_len = max(max_len,j-i+1)
#     return max_len


# #3.better solution for both positive and negative array
# def longest_subarray_sum_k(nums,k):
#     max_length= 0
#     sum=0
#     prefix_sum={}
#     for i in range(len(nums)):
#         sum+=nums[i]
#         if sum == k:
#             max_length = i+1
#         if (sum-k) in prefix_sum:
#             max_length =  max(max_length,(i-prefix_sum[sum-k]))
#         else:
#             prefix_sum[sum] = prefix_sum.get(sum,i)
#     return max_length

#4.sliding window 
#works only if array contain natural numbers
#it cannot contain zero and negative number
def longest_subarray_sum_k(nums,k):
    n = len(nums) # size of the array.

    left, right = 0, 0 # 2 pointers
    Sum = nums[0]
    maxLen = 0
    while right < n:
        # if sum > k, reduce the subarray from left
        # until sum becomes less or equal to k:
        while left <= right and Sum > k:
            Sum -= nums[left]
            left += 1

        # if sum = k, update the maxLen i.e. answer:
        if Sum == k:
            maxLen = max(maxLen, right - left + 1)

        # Move forward the right pointer:
        right += 1
        if right < n: Sum += nums[right]

    return maxLen

            

print(longest_subarray_sum_k([2,0,0,0,3],3))