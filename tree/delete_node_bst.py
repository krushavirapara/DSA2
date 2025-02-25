class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def findmin(root):
            curr = root
            while curr.left:
                curr = curr.left
            return curr
            
        if not root:
            return None
        if root.val>key:
            root.left = self.deleteNode(root.left,key)
        elif root.val<key:
            root.right = self.deleteNode(root.right,key)
        else:
            if not root.left and not root.right:
                return None
            elif not root.left:
                temp = root
                root = root.right
            elif not root.right:
                root = root.left
            else:
                temp = findmin(root.right)
                root.val  = temp.val
                root.right = self.deleteNode(root.right,temp.val)
            return root
        return root
                