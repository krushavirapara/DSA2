# 1335. Minimum Difficulty of a Job Schedule
# Solved
# Hard
# Topics
# Companies
# Hint
# You want to schedule a list of jobs in d days. Jobs are dependent (i.e To work on the ith job, you have to finish all the jobs j where 0 <= j < i).

# You have to finish at least one task every day. The difficulty of a job schedule is the sum of difficulties of each day of the d days. The difficulty of a day is the maximum difficulty of a job done on that day.

# You are given an integer array jobDifficulty and an integer d. The difficulty of the ith job is jobDifficulty[i].

# Return the minimum difficulty of a job schedule. If you cannot find a schedule for the jobs return -1.


#partittion dp
#front partitioning

class solution():

	def minDifficulty(self, nums: List[int], d: int) -> int:
	        n = len(nums)
	        if len(nums)<d:
	            return -1
	        def helper(idx,d):
	            if d==0 and idx==n:
	                return 0
	            if dp[idx][d]!=-1:
	                return dp[idx][d]
	            max_ele = -float("inf")
	            mini = float("inf")
	            temp = float("inf")
	            for i in range(idx,len(nums)):
	                max_ele = max(max_ele,nums[i])
	                if d>0:
	                    temp = max_ele + helper(i+1,d-1)

	                mini = min(mini,temp)
	            dp[idx][d] = mini
	            return dp[idx][d]
	        dp = [[-1 for i in range(d+1)] for j in range(n+1)]
	        return helper(0,d)
