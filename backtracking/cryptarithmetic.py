
def crypt(s1,s2,s3):
    unique = set()
    for ch in s1:
        unique.add(ch)
    for ch in s2:
        unique.add(ch)
    for ch in s3:
        unique.add(ch)
    if len(unique)>10:
        return "Can't form combinations"
    unique = sorted(list(unique))
    used = set()
    ma = {}
    ans=[]
    def is_valid_assignment():
        num1 = int("".join(str(ma[ch]) for ch in s1))
        num2 = int("".join(str(ma[ch]) for ch in s2))
        num3 = int("".join(str(ma[ch]) for ch in s3))
        return num1+num2==num3
    def isvalid(i):
        if i not in used:
            return True
        return False
    def helper(unique,idx,ma,used,ans):
        if idx==len(unique):
            if is_valid_assignment():
                ans.append(ma.copy())
            return
        for i in range(10):
            if isvalid(i):
                ma[unique[idx]] = i
                used.add(i)
                helper(unique,idx+1,ma,used,ans)
                del ma[unique[idx]]
                used.remove(i)
    
    helper(unique,0,ma,used,ans)
    for m in ans:
        print(m)
crypt("send","more","money")
            
            
    