from typing import Optional
from treenode import TreeNode

"""🌳 Return the maximum depth of the binary tree."""
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # 🔍 Calculate the number of nodes along the deepest root-to-leaf path.
        return 0