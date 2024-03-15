# Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

# Return the number of good nodes in the binary tree.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, maxVal):
            if not node:
                return 0

            if node.val >= maxVal:
                res = 1
            else:
                res = 0

            maxVal = max(node.val, maxVal)

            return dfs(node.left, maxVal) + dfs(node.right, maxVal) + res

        return dfs(root, root.val)

        # goodNodes = 1
        # maxVal = root.val
        # stack = [root]

        # while(len(stack)):
        #     curr = stack.pop()
        #     if(curr.left):
        #         if(curr.val <= curr.left.val and curr.left.val >= maxVal):
        #             goodNodes += 1
        #         stack.append(curr.left)
        #     if(curr.right):
        #         if(curr.val <= curr.right.val and curr.right.val >= maxVal):
        #             goodNodes += 1
        #         stack.append(curr.right)

        # return goodNodes
