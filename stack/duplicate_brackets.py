
def findDuplicateparenthesis(string): 

	# create a stack of characters 
	Stack = [] 

	# Iterate through the given expression 
	for ch in string:
	
		# if current character is 
		# close parenthesis ')' 
		if ch == ')': 
		
			# pop character from the stack 
			if Stack[-1]=="(":
			    return True
			else:
    		    while Stack[-1]!="(":
    			    Stack.pop()
    			    
    			
    			Stack.pop()

		# push open parenthesis '(', operators 
		# and operands to stack 
		else:
			Stack.append(ch) 
	
	# No duplicates found 
	return False

# Driver Code
if __name__ == "__main__": 

	# input balanced expression 
	string = "((a+b)(c+d))"

	if findDuplicateparenthesis(string) == True: 
		print("Duplicate Found") 
	else:
		print("No Duplicates Found") 

# This code is contributed by Rituraj Jain
