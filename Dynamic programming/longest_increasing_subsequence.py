class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
       
        # def helper(i,prev):
        #     if i == len(nums):
        #         return 0
        #     if dp[i][prev]!=0:
        #         return dp[i][prev]
        #     take = -float("inf")
        #     if prev == 0  or nums[i]>nums[prev-1]:
        #         take = 1 + helper(i+1,i+1)
        #     non_take = helper(i+1,prev)
        #     dp[i][prev] = max(take,non_take)
        #     return max(take,non_take)
        n = len(nums)
        dp = [[0 for i in range(len(nums)+1)]for j in range(len(nums)+1)]
        
        # # helper(0,0)
        # # print(dp)

        # return dp[0][0]

        # for i in range(n-1,-1,-1):
        #     for prev in range(n,-1,-1):
        #         take = -float("inf")
        #         if prev == 0  or nums[i]>nums[prev-1]:
        #             take = 1 + dp[i+1][i+1]
        #         non_take = dp[i+1][prev]
        #         dp[i][prev] = max(take,non_take)
     
        # return dp[0][0]

        #partition sorting
        #uses binary search hence t.c = o(nlogn)
        import bisect
        temp = []
        for i in range(len(nums)):
            ind = bisect.bisect_left(temp,nums[i],0,len(temp))
            
            if ind==len(temp):
                temp.append(nums[i])
            else:
                temp[ind] = nums[i]
       
        return len(temp)

            