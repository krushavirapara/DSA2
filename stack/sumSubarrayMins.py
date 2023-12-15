def sumSubarrayMins( arr) -> int:
    def nle(arr):
        v=[]
        s=[]
        for i in range(len(arr)):
            if len(s)==0:
                v.append(-1)
            elif s and s[-1][0]<arr[i]:
                v.append(s[-1][1])
            elif s and s[-1][0]>=arr[i]:
                while s and s[-1][0]>=arr[i]:
                    s.pop()
                if len(s)==0:
                    v.append(-1)
                else:
                    v.append(s[-1][1])
            s.append((arr[i],i))


       
        ans = []
        for i in range(len(arr)):
            t = i-v[i]
            ans.append(t)
        return ans

    def gle(arr):

        v = []
        s = []

        # Iterate through the array in reverse order
        for i in range(len(arr) - 1, -1, -1):
            if len(s) == 0:
                v.append(len(arr))
            elif s and s[-1][0] < arr[i]:
                v.append(s[-1][1])
            elif s and s[-1][0] >= arr[i]:
                while s and s[-1][0] >= arr[i]:
                    s.pop()
                if len(s) == 0:
                    v.append(len(arr))
                else:
                    v.append(s[-1][1])
            s.append((arr[i], i))

        # Reverse the list to get the correct order
        v.reverse()

        
        ans = []
        for i in range(len(arr)):
            t = v[i]-i
            ans.append(t)
        return ans

    # Example usage:

    
    l=nle(arr)
   
    r=gle(arr)
    
    ans=[]
    for i in range(len(r)):
        ans.append(arr[i]*l[i]*r[i])
    
    return sum(ans)

print(sumSubarrayMins([11,81,94,43,3]))