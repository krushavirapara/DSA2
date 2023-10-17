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