from iterative import root

def node_to_root(root,no):
	if root.data == no:
		return [no]

	if not root:
		return []

	lf = node_to_root(root.left,no)
	if lf:
		lf.append(root.data)
		return lf

	rf = node_to_root(root.right,no)
	if rf:
		rf.append(root.data)
		return rf

	return []

print(node_to_root(root,70))

def k_levels_down(root,k):
	if not root:
		return []

	if k==0:
		return [root.data]
	ans = []
	lf = k_levels_down(root.left,k-1)
	rf = k_levels_down(root.right,k-1)

	ans.extends(lf)
	ans.extends(rf)
	return ans

print(k_levels_down(root,3))