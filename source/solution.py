"""🌳 Entry point for calculating the maximum depth of a binary tree."""

from typing import Optional
from treenode import TreeNode
from .approaches import Recursion

class Solution:
    """🚀 Select and execute the approach for the tree depth problem."""

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """🔍 Return the maximum depth of the given binary tree."""

        # 🔄 Use the recursive DFS approach to calculate the deepest path.
        recursion: Recursion = Recursion()

        # 📏 Return the maximum number of nodes from root to any leaf.
        return recursion.findMaxDepth(root=root)
