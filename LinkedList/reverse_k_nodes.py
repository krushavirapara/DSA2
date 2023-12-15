#reverse k nodes 
from basics import LinkedList,Node

#https://medium.com/@hiimdaosui/reverse-nodes-in-k-group-9d232e4a70a7#:~:text=Given%20a%20linked%20list%2C%20reverse%20the%20nodes%20of%20a%20linked,should%20remain%20as%20it%20is.


def reverse(head,k):
	temp = head
	count = 0
	while temp:
		count+=1
		if count==2*k:
			break
		temp = temp.next
	if count<2*k:
		return head

	prev = Node()
	next_curr = Node()
	curr= head

	for i in range(k):
		next_curr = curr.next
		curr.next = prev
		prev = curr
		curr = next_curr
	if curr:
		for i in range(k):
			prev=curr
			if curr.next:
				curr = curr.next
	head.next = reverse(curr,k)
	return prev

head = Node(1)
second = Node(2)
head.next = second
second.next = Node(3)
second.next.next = Node(4)
second.next.next.next = Node(5)
second.next.next.next.next = Node(6)

ll = LinkedList(head)
ll.insertAtEnd(Node(7))
ll.insertAtEnd(Node(8))
ll.insertAtEnd(Node(9))
ll.listPrint(head)

r = reverse(head,3)
print()
ll.listPrint(r)

