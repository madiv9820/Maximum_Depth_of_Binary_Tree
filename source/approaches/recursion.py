"""🌳 Recursive Depth-First Search approach for Maximum Depth of Binary Tree.

This module calculates the maximum depth of a binary tree by recursively
exploring its left and right subtrees. For every node, the deeper subtree
determines the longest path from that node to a leaf.
"""

from typing import Optional
from treenode import TreeNode


class Recursion:
    """🔄 Calculate binary tree depth using recursive DFS."""

    def findMaxDepth(self, root: Optional[TreeNode]) -> int:
        """🔍 Return the maximum depth from the given node to any leaf.

        The depth of an empty subtree is zero. For a non-empty node, the
        maximum depth is one for the current node plus the greater depth
        of its left and right subtrees.

        Args:
            root: 🌱 The current node from which depth calculation begins.

        Returns:
            📏 The number of nodes along the longest path from the
            current node to a leaf.
        """

        # 🌱 An empty subtree has no nodes and therefore contributes zero depth.
        maxDepth: int = 0

        if root:
            # ⬅️ Recursively calculate the maximum depth of the left subtree.
            leftDepth: int = self.findMaxDepth(root=root.left)

            # ➡️ Recursively calculate the maximum depth of the right subtree.
            rightDepth: int = self.findMaxDepth(root=root.right)

            # 🌳 Count the current node and extend the deeper subtree by one level.
            maxDepth = 1 + max(leftDepth, rightDepth)

        return maxDepth
