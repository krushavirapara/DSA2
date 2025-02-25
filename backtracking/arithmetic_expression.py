def evaluate(op):
    res = op[0]
    ans = int(op[0])
    for i in range(1,len(op)-1,2):
        if op[i]=="+":
            ans = ans + op[i+1]
        if op[i] == "-":
            ans = ans - op[i+1]
        if op[i] == "*":
            ans = ans*op[i+1]
    
    return ans%101==0
        
        
        
def arithmatic(nums,idx,op,ans):
    if idx == len(nums):
        if evaluate(op):
            ans.append("".join([str(i) for i in op]))
        return 
    for ch in ["+","-","*"]:
        arithmatic(nums,idx+1,op+[ch,nums[idx]],ans)
ans = []
arithmatic([22,79,21],1,[22],ans)
print(ans)