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