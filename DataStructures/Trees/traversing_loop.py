class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
root = Node(1)
root.left = Node(2)  #                  1
root.right = Node(3) #              2       3
root.left.left = Node(4)#       4     7          6
root.right.right = Node(6)# 5     
root.left.left.left = Node(5)
root.left.right = Node(7)

# node = root
# while node.left != None:
#     node = node.left
    
current_node = root
stack = []

while current_node or stack:
    while current_node:
        print(current_node.val)
        stack.append(current_node)
        current_node = current_node.left
    
    current_node = stack.pop()
    # print(current_node.val)
    current_node = current_node.right


    
