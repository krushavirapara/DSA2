class Node:
   def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data

root = Node(12)
root.left = Node(6)
root.right = Node(14)
root.left.left  =Node(3)


def in_order(root):
   if not root:
      return 
   else:
      in_order(root.left)
      print(root.data,end ="->")
      in_order(root.right)

print("In order traversal",end ="  ")
in_order(root)
print()

# class Solution:
#     def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         ans =[]
#         if not root:
#             return ans
#         else:

#             ans.extend(self.inorderTraversal(root.left))
#             ans.append(root.val)
#             ans.extend(self.inorderTraversal(root.right))
#             return ans



#Iterative
# class Solution:
#     def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         if not root:
#             return []
#         ans = []
#         stack =[root]
#         while stack:
#             if stack[-1].left:
#                 stack.append(stack[-1].left)
#             else:
#                 ans.append(stack[-1].val)
#                 temp = stack.pop()
#                 if stack:
#                     stack[-1].left = None
#                 if temp.right:
#                     stack.append(temp.right)
#         return ans