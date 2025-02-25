s = [1, 3, 0, 5, 8, 5]
f = [2, 4, 6, 7, 9, 9]
def printMaxActivities(s,f):
    li = [[i,j] for i,j in zip(s,f)]
    li = sorted(li,key =lambda x: x[1])
    print(li)
    print(0)
    finish = li[0][1]
    for i in range(1,len(li)):
        if li[i][0]>finish:
            print(i)
            finish = li[i][1]

printMaxActivities(s, f)

def findMin(n):
    coins = [1,2,5,10,20,50,100,500,1000]
    ans =[]
    for i in range(len(coins)-1,-1,-1):
        while coins[i]<=n:
            n = n-coins[i]
            ans.append(coins[i])
    return ans
n = 93

print("Following is minimal number",
      "of change for", n, ": ", end = "")
print(findMin(n))

# it will work for denominations where sum of two previous denominations is less than next denomination
#it will not work for [1,5,6,9] and n=11

def solve(arr):
    arr.sort()
    num1 = str(arr[0])
    num2 = str(arr[1])
    i,j = 2,3
    print(len(arr)//2+1)
    while i<len(arr):
        num1+=str(arr[i])
        if j<len(arr):num2+=str(arr[j])
        i+=2
        j+=2
    return int(num1),int(num2)
arr = [ 6, 8, 4, 5, 2,  ]
print("The required sum is ", solve(arr))

a = [4, 1, 8, 7]
b = [2, 3, 6, 5]
n = len(a)
def findMinSum(a,b,n):
    a.sort()
    b.sort()
    ans=0
    for i,j in zip(a,b):
        ans+=abs(i-j)
    return ans
print(findMinSum(a, b, n)

boxes= [40,20,100,30]
n = len(boxes)
def maxLevel(boxes,n):
    level = 0
    boxes.sort()
    prev = boxes[0]
    level = 1
    prev_n = 1
    curr_w = 0
    curr_n = 0
    for i in range(1,len(boxes)):
        curr_w+=boxes[0]
        curr_n+=1
        if curr_w>prev and curr_n>prev_n:
            prev = curr_w
            prev_n = curr_n
            curr_w=0
            curr_n=0
            level+=1
    return level
        
        
print(maxLevel(boxes, n))
#you can use binary search alaso to find required elements and proceed further