from collections import Counter
def count_unique_substring(s,k):
	i=0
	j=0
	count=0
	while j<len(s):
		if (j-i+1)<k:
			j+=1
		elif(j-i+1==k):
			sub = s[i:j+1]
			if len(Counter(sub))==k:
				count+=1
			j+=1
			i+=1
	return count

print(count_unique_substring("aacfssa",3))