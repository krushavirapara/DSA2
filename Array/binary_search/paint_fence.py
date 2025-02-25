# thhis is line sweep problem bhul thi aama save thai gyu

def painte_fence(intervals):
    res= []
    painted = {}
    
    for start,end in intervals:
        work = 0
        while start<end:
            if start in painted:
                temp = painted[start]
                painted[start] = max(painted[start],end)
                start = temp
                
            else:
                painted[start] = end
                start+=1
                work+=1
        res.append(work)
    return res
    
print(painte_fence([[1,4],[5,9],[4,7]]))

# def is_valid(mid):
    

# def smallest_kth_distance(nums):
#     nums.sort()
#     low = 0 
#     high = arr[-1]-arr[0]
#     ans = float("inf")


#     while low<=high:
#         mid = (low+high)//2

#         if is_valid(mid):
#             low = mid+1
#         else :
#             right = mid-1