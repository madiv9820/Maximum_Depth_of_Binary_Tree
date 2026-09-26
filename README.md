# [🌳 Tracing the Deepest Branch](https://leetcode.com/problems/maximum-depth-of-binary-tree/?envType=study-plan-v2&envId=top-interview-150)

Imagine you're exploring a **tree-shaped maze** 🧭🌲—starting at the root, you want to know how many levels you can travel before reaching the farthest leaf. Your task is to find the **maximum depth**, i.e., the number of nodes along the longest path from the root to any leaf.

#### 📌 Example 

- **📌 Example 1 — Balanced Branching**

    ![](https://assets.leetcode.com/uploads/2020/11/26/tmp-tree.jpg)

    ```
    Input:  root = [3,9,20,null,null,15,7]
    Output: 3
    ```

    The longest path is **`3 → 20 → 15`** (or **`3 → 20 → 7`**), containing **3 nodes**.

- **📌 Example 2 — Single Branch**

    ```
    Input:  root = [1,null,2]
    Output: 2
    ```

    The path **`1 → 2`** contains **2 nodes**, so the maximum depth is **`2`**.

#### ⚙️ Constraints

- **`0 ≤ number of nodes ≤ 10⁴`**
- **`-100 ≤ Node.val ≤ 100`**

---

### 🌳 Approaches

There are multiple ways to measure the depth of a binary tree, but the core idea remains the same: **find the farthest leaf from the root**. 🌱📏 We can either let recursion explore the tree naturally, maintain our own stack for DFS, or count the tree level-by-level using BFS.

- #### 🔄 Recursion

    - **Intuition:** Think of every node asking its children, *“How deep can you go from here?”* 🤔🌳 Once both answers return, the node keeps the deeper path and adds itself to the depth.

    - **Steps:**

        1. If the current node is None, return 0.
        2. Recursively find the depth of the left subtree.
        3. Recursively find the depth of the right subtree.
        4. Take the larger depth and add 1 for the current node.

    - **Pseudocode:**

        ```
        FUNCTION depth(node):
            IF node is null:
                RETURN 0

            leftDepth  = depth(node.left)
            rightDepth = depth(node.right)

            RETURN 1 + max(leftDepth, rightDepth)
        ```

    - **Complexity:**

        - **⏱️ Time: `O(n)`**
        - **💾 Space: `O(h)`** — recursion stack, where **`h`** is tree height.

- #### 📚 Traversal

    - **Intuition:** What recursion does behind the scenes can be done explicitly with a **stack**. Instead of letting function calls remember where we are, we store each node along with its depth ourselves. 🔄

    - **Steps:**

        1. Push the root with depth **`1`** onto a stack.
        2. Pop a node and record its depth.
        3. Push its children with **`depth + 1`**.
        4. Continue until the stack is empty.
        5. Keep the largest depth encountered.
    
    - **Pseudocode:**

        ```
        IF root is null:
            RETURN 0

        PUSH (root, 1) into stack

        WHILE stack is not empty:
            node, depth = POP stack

            maxDepth = max(maxDepth, depth)

            IF node.left exists:
                PUSH (node.left, depth + 1)

            IF node.right exists:
                PUSH (node.right, depth + 1)

        RETURN maxDepth
        ```

    - **Complexity:**

        - **⏱️ Time: `O(n)`**
        - **💾 Space: `O(h)`** — DFS stack in terms of tree height.

- #### 🌊 Levels

    - **Intuition:** Instead of chasing individual paths, look at the tree **one level at a time**. Every completed level means we've moved one step deeper into the tree. When there are no more levels, the number of levels is the maximum depth. 📏🌳

    - **Steps:**

        1. If the tree is empty, return **`0`**.
        2. Add the root to a queue.
        3. Process every node belonging to the current level.
        4. Add their children to the next level.
        5. Increase depth after completing the level.
        6. Repeat until the queue is empty.
    
    - **Pseudocode:**

        ```
        IF root is null:
            RETURN 0

        PUT root into queue
        depth = 0

        WHILE queue is not empty:
            PROCESS all nodes in current level

            FOR each node:
                ADD its children to queue

            depth = depth + 1

        RETURN depth
        ```
    
    - **Complexity:**

        - **⏱️ Time: `O(n)`**
        - **💾 Space: `O(w)`** — where **`w`** is the maximum width of the tree.

### 📊 Quick Comparison

| Approach         | Core Idea                    |   Time |  Space |
| ---------------- | ---------------------------- | -----: | -----: |
| 🔄 **Recursion** | Ask subtrees for their depth | **`O(n)`** | **`O(h)`** |
| 📚 **Traversal** | DFS with an explicit stack   | **`O(n)`** | **`O(h)`** |
| 🌊 **Levels**    | Count levels using BFS       | **`O(n)`** | **`O(w)`** |

**💡 Interesting takeaway:** All three visit every node exactly once. The real difference is **how they remember where they are** — recursion uses the call stack, Traversal uses an explicit stack, and Levels uses a queue. 🚀🌳

---
