#leetcode 2483

#this will run into TLE
def bestClosingTime(customers: str) -> int:
    def check_penalty(hour):
        penalty = 0
        for j in range(hour):
            if customers[j]=="N":
                penalty+=1
        for j in range(hour,len(customers)):
            if customers[j]=="Y":
                penalty+=1
        return penalty
    p=[]
    for i in range(len(customers)+1):
        p.append(check_penalty(i))
    return p.index(min(p))
        
print(bestClosingTime("YYNY"))

#2.Better Approach
def bestClosingTime(customers: str) -> int:
    n = len(customers)
    prefix_sum  = [0]*(n+1)
    postfix_sum = [0]*(n+1)

    for i in range(1,n+1):
        prefix_sum[i] = prefix_sum[i-1]
        if customers[i-1]=="N":
            prefix_sum[i]+=1
        
    for i in range(n-1,-1,-1):
        postfix_sum[i] = postfix_sum[i+1]
        if customers[i]=="Y":
            postfix_sum[i]+=1
       
    min_penalty,idx = float('inf'),0
    for i in range(n+1):
         p = prefix_sum[i]+postfix_sum[i]
         if p < min_penalty:
            min_penalty=p
            idx = i
    return idx

print(bestClosingTime("YYNY"))