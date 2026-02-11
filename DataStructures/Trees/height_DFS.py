def height(node):
    if node is None:
        return 0

    left_h = height(node.left)
    right_h = height(node.right)

    return 1 + max(left_h, right_h)
