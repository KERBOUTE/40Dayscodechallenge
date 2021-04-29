class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

# function to check if it is leaf node
def isLeaf(node):
    if node is None:
        return False
    if node.left is None and node.right is None:
        return True
    return False

# recursive function to find the sum of all left leaf nodes
def sum_leaf(root):

    res = 0
    if root:

        if isLeaf(root.left):
            res += root.left.data
        else:
            res += sum_leaf(root.left)

        res += sum_leaf(root.right)

    return res

# driver function
if __name__ == '__main__':
    root = Node(20)
    root.left = Node(9)
    root.right = Node(49)
    root.right.left = Node(23)
    root.right.right = Node(52)
    root.right.right.left = Node(50)
    root.left.left = Node(5)
    root.left.right = Node(12)
    root.left.right.right = Node(12)
    print(sum_leaf(root))
