from typing import Optional

"""🌳 Represents a single node in a binary tree."""
class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: Optional[TreeNode] = None,
        right: Optional[TreeNode] = None,
    ) -> None:
        # 📦 Store the value held by this node.
        self.val: int = val

        # ◀️ Reference to the left child, if present.
        self.left: Optional[TreeNode] = left

        # ▶️ Reference to the right child, if present.
        self.right: Optional[TreeNode] = right
