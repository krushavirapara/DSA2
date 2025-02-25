



def post_order(root):
   if not root:
      return 
   else:
      post_order(root.left)
      post_order(root.right)
      print(root.data,end ="->")

print("Post order traversal",end ="  ")
post_order(root)
print()

# class Solution:
#     def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         ans =[]
#         if not root:
#             return ans
#         else:
#             ans.extend(self.postorderTraversal(root.left))
#             ans.extend(self.postorderTraversal(root.right))
#             ans.append(root.val)
#             return ans




