class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return None
        else:
            res = [root.val]
            stack = [root]
            while stack:
                new_stack = []
                for s in stack:
                    if s.left:
                        new_stack.append(s.left)
                    if s.right:
                        new_stack.append(s.right)
                if new_stack:
                    res.append(new_stack[-1].val)
                stack = new_stack
            return res
