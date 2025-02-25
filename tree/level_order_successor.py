def level_order_successor(root,x):
	if not root:
		return None

	queue =[root]
	while queue:
		temp = queue[0]
		queue.remove(temp)
		if temp.left:
			queue.append(temp.left)
		if temp.right:
			queue.append(temp.right)
		if temp.val==x:
			return queue[0]
	return None