class Node:
   def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data

root = Node(12)
root.left = Node(6)
root.right = Node(14)
root.left.left  =Node(3)


def prety(node,level):
   if not node:
      return 
   prety(node.right,level+1)
   if level!=0:
      print("|\t" * (level - 1), end="")
      print("|------>",node.data)
   else:
      print(node.data)
   prety(node.left,level+1)

prety(root,0)


def pre_order(root):
   if not root:
      return 

   else:
      print(root.data,end ="->")
      pre_order(root.left)
      pre_order(root.right)

print("pre order traversal",end ="  ")
pre_order(root)
print()

# class Solution:
#     def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         ans =[]
#         if not root:
#             return ans
#         else:
#             ans.append(root.val)
#             ans.extend(self.preorderTraversal(root.left))
#             ans.extend(self.preorderTraversal(root.right))
#             return ans

#iterative solution
# class Solution:
#     def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         if not root:
#             return []
#         ans = []
#         stack =[root]
#         while stack:
#             temp = stack.pop()
#             ans.append(temp.val)
#             if temp.right:
#                 stack.append(temp.right)
#             if temp.left:
#                 stack.append(temp.left)