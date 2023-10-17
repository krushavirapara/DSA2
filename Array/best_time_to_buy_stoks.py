from typing import List
#leetcode 121
def maxProfit(prices: List[int]) -> int:
    nums=prices
    max_profit = 0 
    buy = float('inf')
    sell = 0 
    for i in range(len(nums)):
        buy = min(buy,nums[i])
        if nums[i]>buy:
            sell= nums[i]
            max_profit = max(max_profit,sell-buy)
            
    return max_profit

print(maxProfit([7,1,5,3,6,4]))