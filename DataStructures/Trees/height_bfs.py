from collections import deque

def height_bfs(root):
    if not root:
        return 0

    q = deque([root])
    height = 0

    while q:
        level_size = len(q)

        for _ in range(level_size):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        height += 1

    return height

'''7️⃣ DFS vs BFS for height
Method	Uses	When to use
DFS	Recursion	Most common
BFS	Queue	Level-based logic

In interviews, DFS is preferred unless asked otherwise.

8️⃣ Time & Space Complexity (must say)

Time: O(n) (visit every node once)

Space:

DFS: O(h) (call stack)

BFS: O(w) (queue width)

🎤 Interview-perfect explanation

Say this:

“Height is computed bottom-up using recursion. For each node, I calculate the height of its left and right subtrees and return one plus the maximum of those values.”

This is textbook-perfect.

🔥 What height unlocks next

Now you’re ready for:

Balanced tree check

Diameter of tree

Max path sum
'''
These all reuse this exact pattern.
