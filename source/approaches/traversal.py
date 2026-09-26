from treenode import TreeNode
from typing import Optional, List, Tuple

"""🔄 Iterative Depth-First Search approach for Maximum Depth of Binary Tree.

This module calculates the maximum depth of a binary tree using an explicit
stack. Each stack entry stores a tree node together with its current depth,
allowing DFS traversal without relying on recursive function calls.
"""

from typing import List, Optional, Tuple
from treenode import TreeNode


class Traversal:
    """🔄 Calculate binary tree depth using iterative DFS."""

    def findMaxDepth(self, root: Optional[TreeNode]) -> int:
        """🔍 Return the maximum depth from the root to any leaf.

        The tree is traversed using an explicit stack instead of recursion.
        Each entry contains a node and its depth from the root. Whenever a
        node is visited, its depth is compared with the maximum depth found
        so far. Its children are then added to the stack with their depth
        increased by one.

        Args:
            root: 🌱 The root node of the binary tree.

        Returns:
            📏 The number of nodes along the longest path from the root
            to any leaf.
        """

        # 🌱 An empty tree contains no nodes and therefore has depth zero.
        maxDepth: int = 0

        if root:
            # 📚 Store each node together with its depth from the root.
            nodeStack: List[Tuple[TreeNode, int]] = [(root, 1)]

            while nodeStack:
                # 🔄 Remove the latest node to perform depth-first traversal.
                currentNode, currentDepth = nodeStack.pop()

                # 📏 Update the maximum depth reached so far.
                maxDepth = max(maxDepth, currentDepth)

                # ⬅️ Add the left child at the next depth level.
                if currentNode.left:
                    nodeStack.append(
                        (currentNode.left, currentDepth + 1)
                    )

                # ➡️ Add the right child at the next depth level.
                if currentNode.right:
                    nodeStack.append(
                        (currentNode.right, currentDepth + 1)
                    )

        return maxDepth
