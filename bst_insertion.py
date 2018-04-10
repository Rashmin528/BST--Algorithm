class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def insert(root, node):
    if root is None:
        root = node
    else:
        if root.data > node.data:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)
            
        else:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)

def in_order(root):
    if not root:
        return
    in_order(root.left)
    print root.data
    in_order(root.right)

root = Node(12)
insert(root, Node(10))
insert(root, Node(8))
insert(root, Node(99))
insert(root, Node(62))
insert(root, Node(54))
insert(root, Node(26))
insert(root, Node(30))
insert(root, Node(4))
insert(root, Node(171))
insert(root, Node(0))

print in_order(root)

