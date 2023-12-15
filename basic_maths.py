def countDigits(n: int) -> int:
    cnt=0
    d=n
    while(n>0):
        rem = n%10
        if(d%rem==0 and rem!=0):
            cnt+=1
        n=int(n/10)
        
    return cnt

print(countDigits(35))

def reverse(n):
    ans =0
    while n>0:
        r = n%10
        n=int(n/10)
        ans =ans*10+r
    return ans

print( reverse(35))

def isPalindrome(n):
    if n==reverse(n):
        return True
    else:
        return False
    
print(isPalindrome(432))

