from constructor import adj,n
#print(adj)


visited = [False for i in range(n+1)]

parent = [-1 for i in range(n + 1)]


#simple dfs 
#time complexity = O(V+E)
#v = number of vertices
#e = number of edges
def simple_dfs(vertex):
	print(vertex, end = " ")
	visited[vertex] = True
	for child in adj[vertex]:
		if not visited[child]:
			simple_dfs(child)

# print("dfs traversal is : " ,end = " ")
# simple_dfs(1)
# print()
# print("**********************************************")
#print()


def connected_components(n):
	count = 0
	for i in range(1,n+1):
		if not visited[i]:
			count+=1
			simple_dfs(i)
			print()
	return count


#print("Number of connected components are : ", connected_components(n))
#print("****************************************************")
#print()


# #cycle_detection
def dfs(vertex,par):
    visited[vertex] = True
    loopexists = False
    for neigh in adj[vertex]:
    
        if visited[neigh] and neigh==par:
            continue
        elif visited[neigh] and neigh!=parent[vertex]:
            return True
        loopexists = loopexists or dfs(neigh,vertex)
    return loopexists

# adj[1].append(5)
# adj[5].append(1)
# print("cycle exists or not: ",dfs(1,-1))
# print("********************************")
# print()

