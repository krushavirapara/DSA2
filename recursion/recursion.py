def printNum(n):
    if n==0:
        return
    else:
        printNum(n-1)
        print(n)
        

printNum(5)
print()

def printRevNum(n):
    if n==0:
        return
    else:
        print(n)
        printRevNum(n-1)
        

printRevNum(5)
print()


def printSum(n):
    if n==0:
        return 0
    else:
        return n + printSum(n-1)
    
print(printSum(5))

def fact(n):
    if n==1:
        return n
    else:
        return n*fact(n-1)

print(fact(5))

s=[1,2,3,4,5]
n=len(s)-1
def revArray(i):
    if i >= (n-i):
        return
    else:
        s[i],s[n-i] = s[n-i],s[i]
        revArray(i+1)
revArray(0)
print(s)

s="krusha"
n=len(s)-1
def isPAlindrome(i):
    if i>=(n-i):
        return True
    elif s[i]!=s[n-i]:
        return False
    else:
        return isPAlindrome(i+1)


print(isPAlindrome(0))

def fibb(n):
    if n<2:
        return n
    else:
        return fibb(n-1) + fibb(n-2)

print(fibb(6))


#decimal to binary
def db(n):
    if n==0 or n==1:
        return n
    else:
        return str(db(n//2)) + str(n%2)
        
print(db(19))


#reverse a string
def rev_str(s):
    if not s:
        return 0
    else:
        return 1 + rev_str(s[1:])
        
print(rev_str("a"))

#find fibbonacci number
def fibb(n):
    if n<2:
        print(n)
        return
    else:
        print(fibb(n-1))

#min and max element from array       
def min_max(arr):
    if len(arr)==1:
        return arr[0],arr[0]
    else:
        tmp = arr [-1]
        loc_min,loc_max = min_max(arr[:-1])
        return min(tmp,loc_min),max(tmp,loc_max)
        
print(min_max([1,4,3,-6,-4,8,16]))

#check if palindrome or not
def palindrome(s):
    return helper(s,0,len(s)-1)

def helper(s,start,end):
    if start == end:
        return True
    else:
        if s[start]==s[end] and start<=end:
            return helper(s,start+1,end-1)
        if start>end:
            return 
        else:
            return False
            
print(palindrome("12321"))

#count no of zeros
def count(arr):
    return h(arr,0,0)
def h (arr,c,i):
    if i==len(arr):
        return c
    else:
        if arr[i]==0:
            c+=1
        return h(arr,c,i+1)
        
print(count([3,0,2,0,4,0]))

#remove "A" from string
def remove_A(s):
    if len(s)==0:
        return ""
    else:
        temp = remove_A(s[1:])
        if s[0]!="a":
            temp=s[0]+temp
        return temp        
        
print(remove_A("baccad"))

#no of ways of dice roll for a given target
def dice(op,target):
    ans=[]
    
    if target == 0:
        ans.append(op)
        return ans
        
        
    else:
        for i in range(1,7):
            if i<=target:
                t = dice(op+str(i),target-i)
                ans.extend(t)
        return ans
        
print(len(dice("",4)))


#number of awys to achieve get specified amount from given change
def coin_change(arr,target,op):
    t=0
    if target == 0:
        print(op)
        return 1
    
    else:
        for i in arr:
            if i<=target:
                temp = count_ways(arr,target-i,op+str(i))
                t+=temp
        return t
                
print(coin_change([1,2,3],4,"")) //7
        