"""🌳 Entry point for calculating the maximum depth of a binary tree."""

from typing import Optional
from treenode import TreeNode
from .approaches import Recursion, Traversal, Levels

class Solution:
    """🚀 Select and execute the approach for the tree depth problem."""

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """🔍 Return the maximum depth of the given binary tree."""

        # 🔄 Use the recursive DFS approach to calculate the deepest path.
        recursion: Recursion = Recursion()

        # 🔄 Initialize the selected iterative DFS approach.
        traversal: Traversal = Traversal()

        # 🌊 Use level-order traversal to count the tree's depth.
        levels: Levels = Levels()

        # 📏 Return the maximum number of nodes from root to any leaf.
        return levels.findMaxDepth(root=root)
