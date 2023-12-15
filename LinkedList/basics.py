class Node:
	def __init__(self,data=None):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self,head=None):
	 	self.head = head

	def listPrint(self,head=None):
		if not head:
	 		temp = self.head
		else:
			temp=head
 			
		while temp is not None:
			print(str(temp.data) + "->",end='')
			temp = temp.next
		print()

	def insertAtBeginning(self,node):
	 	node.next = self.head
	 	self.head = node

	def insertAtEnd(self,node):
		if not self.head:
			self.insertAtBeginning(node)
		else:
			temp =  self.head
			while temp.next:
				temp = temp.next
			temp.next = node

	def RecursiveInsertion(self,index,value,node):
		if index==0:
			new_node  = Node(value)
			new_node.next = node
			return new_node
		else:
			node.next = self.RecursiveInsertion(index-1,value,node.next)
			return node

	# def rec2(self,index,value,node):
	# 	if index==1:
	# 		new_node = Node(value)
	# 		new_node.next = node.next
	# 		node.next = new_node
	# 		return
	#     elif index == 0:
	#         new_node = Node(value)
	#         new_node.next = node
	#         self.head = new_node
	#         return 
	        
	#     elif index>1:
	#         self.rec2(index-1,value,node.next)





if __name__ == "__main__":

	first = Node(4)
	ll = LinkedList()
	ll.head = first
	first.next  = Node(5)
	ll.listPrint()
	ll.insertAtBeginning(Node(3))
	ll.listPrint()




