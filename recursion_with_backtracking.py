# recursion with backtracking


def count_no_of_ways(row,col):
	if row==0 or col==0:
		return 1
	else:
		return count_no_of_ways(row-1,col) + count_no_of_ways(row,col-1)

print(count_no_of_ways(4,4))

def pattern(op,r,c):
    ans = []
    if r==1  and c==1:
        ans.append(op)
        return ans
    
    else:
        if r>1:
            down = pattern(op+"D",r-1,c)
            ans.extend(down)
        if c>1:
            
            right  = pattern(op+"R",r,c-1)
        
            ans.extend(right)
        return ans
        
print(pattern("",r,c))


#with diagonal
def diag(r,c,op):

	ans=[]
	if r==1 and c==1:
		ans.append(op)
		return ans
	else:
		if r>1:
			ans.extend(diag(op+"V",r-1,c))
		if c>1:
			ans.extend(diag(op+"H",r,c-1))
		if r>1 and c>1:
			ans.extend(diag(op+"D",r-1,c-1))
	return ans






