class Node:
   def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data

root = Node(12)
root.left = Node(6)
root.right = Node(14)
root.left.left  =Node(3)

def level_order(root):
   queue = [root]

   while queue:
      temp = queue[0]
      queue.remove(temp)
      print(temp.data,end = "->")
      if temp.left:
         queue.append(temp.left)
      if temp.right:
         queue.append(temp.right)


print("Level order traversal",end ="  ")
level_order(root)
print()


# class Solution:
#     def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         if not root:
#             return []
#         queue = [root]
#         res=[]
#         while queue:
#             size = len(queue)
#             ans =[]
#             for i in range(len(queue)):
#                 temp = queue[0]
#                 ans.append(temp.val)
#                 queue.remove(temp)
#                 if temp.left:
#                     queue.append(temp.left)
#                 if temp.right:
#                     queue.append(temp.right)
#             res.append(ans)
#         return res

#LEETCODE 116
# class Solution:
#     def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
#         if not root:
#             return None
#         queue = [root]
#         ans=[]
#         while queue:
#             size = len(queue)
#             for i in range(len(queue)):
#                 temp = queue[0]
#                 queue.remove(temp)
                
#                 if i==size-1:
#                     temp.next=None
#                 else:
#                     temp.next=queue[0]
#                 if temp.left:
#                     queue.append(temp.left)
#                 if temp.right:
#                     queue.append(temp.right)
                    
#         return root

#LEETCODE 199 -GIVE ONLY RIGHT MOST ELEMENT OF EVERY LEVEL
# class Solution:
#     def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
#         if not root:
#             return []
#         queue = [root]
#         res=[]
#         while queue:
#             size = len(queue)
#             res.append(queue[-1].val)
#             for i in range(len(queue)):
#                 temp = queue[0]
#                 queue.remove(temp)
#                 if temp.left:
#                     queue.append(temp.left)
#                 if temp.right:
#                     queue.append(temp.right)
            
#         return res
#            