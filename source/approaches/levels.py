"""🌊 Level-order traversal approach for Maximum Depth of Binary Tree.

This module calculates the maximum depth of a binary tree by traversing
the tree level by level using a queue. Each completed level represents
one additional depth in the tree.
"""

from typing import List, Optional
from treenode import TreeNode

class Levels:
    """🌊 Calculate binary tree depth using level-order traversal."""

    def findMaxDepth(self, root: Optional[TreeNode]) -> int:
        """🔍 Return the maximum depth by counting tree levels.

        The tree is traversed one level at a time. After all nodes belonging
        to the current level are processed, the depth is increased by one.
        Once the queue becomes empty, every level has been visited.

        Args:
            root: 🌱 The root node of the binary tree.

        Returns:
            📏 The number of levels in the binary tree.
        """

        # 🌱 An empty tree has no levels and therefore has depth zero.
        maxDepth: int = 0

        if root:
            # 📚 Store nodes waiting to be processed level by level.
            nodeQueue: List[TreeNode] = [root]
            queueIndex: int = 0

            while queueIndex < len(nodeQueue):
                # 📏 Capture the boundary of the current level.
                levelEnd: int = len(nodeQueue)

                # 🔄 Process every node belonging to this level.
                while queueIndex < levelEnd:
                    currentNode: TreeNode = nodeQueue[queueIndex]
                    queueIndex += 1

                    # ⬅️ Add the left child to the next level.
                    if currentNode.left:
                        nodeQueue.append(currentNode.left)

                    # ➡️ Add the right child to the next level.
                    if currentNode.right:
                        nodeQueue.append(currentNode.right)

                # 🌊 One complete level has now been traversed.
                maxDepth += 1

        return maxDepth
