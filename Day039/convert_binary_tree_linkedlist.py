

class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def flatten(root):

    # if root is NUll or if leaf node then return
    if root == None or (root.left == None and root.right == None):
        return

    # if root.left exists, then we have to make it root.right
    if root.left != None:

        # move left recursive
        flatten(root.left)

        # store the root.right node
        temp = root.right
        # fix the right so that left subtree rooted at root comes at right of it
        root.right = root.left
        # nullify the left part
        root.left = None

        # now we store the newly fixed right node
        ptr = root.right
        # find the position where we need to attach the previously stored temp (older right node )
        while ptr.right:
            ptr = ptr.right

        # attach the older right to the right of new right (making it flattened)
        ptr.right = temp

    # recurisvely call for right subtree
    flatten(root.right)


from collections import deque

def flatten_list(root):

    stack = deque()
    ptr = root
    while root or stack:

        if root.right:
            stack.append(root.right)

        root.right = root.left
        root.left = None

        if root.right == None and stack:
            root.right = stack.pop()

        root = root.right

    return ptr

# helper function to print inorder traversal
def inorder(root):

    if root == None:
        return

    inorder(root.left)
    print(root.data, end= " ")
    inorder(root.right)

# driver test function
if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(5)
    root.left.left = Node(3)
    root.left.right = Node(4)
    root.right.right = Node(6)
    inorder(root)
    flatten_list(root)
    print()
    inorder(root)
