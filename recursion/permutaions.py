def all_permuations(op,ip,ans):
	if len(ip)==0:
		ans.append(op)
		return ans 
	else:
		for i in range(len(op)+1):
			all_permuations(ip[:i]+ip[0]+ip[i:],ip[1:],ans)
		return ans
print(all_permuations("","abc",[]))

#unique permuations
def all_permuations(op,ip,ans):
    if len(ip)==0:
        ans.add(op)
        return ans 
    else:
       
        for i in range(len(op)+1):
            all_permuations(op[:i]+ip[0]+op[i:],ip[1:],ans)
        return ans
print(all_permuations("","aac",set()))