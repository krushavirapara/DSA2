#2864
class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count=0
        for i in s:
            if i=="1":
                count+=1
        ans = "1"*(count-1) + "0"*(len(s)-count) +"1"
        return ans


#977
def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # Find the index of the first non-negative number
        positive_idx = 0
        while positive_idx < n and nums[positive_idx] < 0:
            positive_idx += 1

        # Initialize two pointers: one for negative numbers and one for non-negative numbers
        neg_ptr = positive_idx - 1
        pos_ptr = positive_idx

        # Initialize an empty list to store the sorted squares
        ans = []

        # Merge the squares of negative and non-negative numbers
        while neg_ptr >= 0 and pos_ptr < n:
            if nums[neg_ptr] * nums[neg_ptr] < nums[pos_ptr] * nums[pos_ptr]:
                ans.append(nums[neg_ptr] * nums[neg_ptr])
                neg_ptr -= 1
            else:
                ans.append(nums[pos_ptr] * nums[pos_ptr])
                pos_ptr += 1

        # Add the remaining squares of negative numbers, if any
        while neg_ptr >= 0:
            ans.append(nums[neg_ptr] * nums[neg_ptr])
            neg_ptr -= 1

        # Add the remaining squares of non-negative numbers, if any
        while pos_ptr < n:
            ans.append(nums[pos_ptr] * nums[pos_ptr])
            pos_ptr += 1

        return ans

#948
def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        l=0
        r=len(tokens)-1
        score=0
        max_score=0
        while l<=r:
            if tokens[l]<=power:
                score+=1
                max_score = max(score,max_score)
                power-=tokens[l]
                l+=1
            elif score>0:
                power+=tokens[r]
                r-=1
                score-=1
            else:
                break
        return max_score
#1750
 def minimumLength(self, s: str) -> int:
        prefix=0
        suffix=len(s)-1
        while prefix<suffix and s[prefix]==s[suffix]:
            c=s[prefix]
            while prefix<=suffix and s[prefix]==c:
                prefix+=1
            while suffix>prefix and s[suffix]==c:
                suffix-=1
        return suffix-prefix+1

def funcll(head):
    if not head:
        return False
    slow = head
    fast = head
    while fast and fast.next:
        
        slow=slow.next
        fast=fast.next.next
        if slow==fast:
            return True
    else:
        return False
            

def maxFrequencyElements(self, nums: List[int]) -> int:
    max_f = 0
    total = 0
    frequencies={}
    for i in nums:
        frequencies[i] = frequencies.get(i,0)+1
        f = frequencies[i]
        if f>max_f:
            max_f = f
            total = max_f
        elif f==max_f:
            total+=f
    return total

def customSortString(self, order: str, s: str) -> str:
        cmap={}
        for i in s:
            cmap[i] = cmap.get(i,0) +1
        res=""
        for o in order:
            if o in cmap:
                res += o * cmap[o]
                del cmap[o]
        for i,j in cmap.items():
            res+=i*j
        return res
            
#confidence level and confidence interval