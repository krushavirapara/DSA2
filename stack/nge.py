# nearest smallest element to left
def immediateSmaller(a) :
    v=[]
    s=[]
    for i in range(len(a)):
        if len(s)==0:
            v.append(-1)
        elif len(s)>0 and a[i]>s[-1]:
            v.append(s[-1])
        elif len(s)>0 and a[i]<=s[-1]:
            while len(s)>0 and a[i]<=s[-1]:
                s.pop()
            if len(s)==0:
                v.append(-1)
            else:
                v.append(s[-1])
        s.append(a[i])
    return v
print(immediateSmaller([4,7,8,2,3,1]))


#nearest greater element to right 
def nearest_greater(nums1,nums2):
    s=[]
    mapping = {}

    for i in range(len(nums2)-1,-1,-1):
        if len(s)==0:
            mapping[nums2[i]]=-1
        elif len(s)>0 and nums2[i]>s[-1]:
            while len(s)>0 and nums2[i]>=s[-1]:
                s.pop()
            if len(s)==0:
                mapping[nums2[i]]=-1
            else:
                mapping[nums2[i]]=s[-1]
        elif len(s)>0 and nums2[i]<s[-1]:
            mapping[nums2[i]] = s[-1]
            
        s.append(nums2[i])
    res =[]
    for i in nums1:
        res.append(mapping[i])
    return res

    

print(nearest_greater([1,4,2],[1,3,4,2]))



#next greatest element for circular array
def nextGreaterElements(nums) :
    s=[]
    v =[]
    for i in range(len(nums)-2,-1,-1):
        if len(s)==0:
            s.append(nums[i])
        elif len(s)>0 and nums[i]<s[-1]:
            s.append(nums[i])
        elif len(s)>0 and nums[i]>=s[-1]:
            while len(s)>0 and s[-1]<=nums[i]:
                s.pop()
            s.append(nums[i])
        

    for i in range(len(nums)-1,-1,-1):
        if len(s)==0:
            v.append(-1)
        elif len(s)>0 and nums[i]>=s[-1]:
            while len(s)>0 and nums[i]>=s[-1]:
                s.pop()
            if len(s)==0:
                v.append(-1)
            else:
                v.append(s[-1])
        elif len(s)>0 and nums[i]<s[-1]:
            v.append(s[-1])
            
        s.append(nums[i])  
        
    return v[::-1]

print(nextGreaterElements([5,4,3,2,1]))




