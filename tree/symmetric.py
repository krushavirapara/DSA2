#LEETCODE 101

#good question
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        queue=[root.left]
        queue.append(root.right)
        while queue:
            left = queue.pop(0)
            right = queue.pop(0)
            
            if left==None and right==None:
                continue
            elif left==None or right==None:
                return False
            elif left.val!=right.val:
                return False
            queue.append(left.left)
            queue.append(right.right)
            queue.append(left.right)
            queue.append(right.left)
            
            
        return True