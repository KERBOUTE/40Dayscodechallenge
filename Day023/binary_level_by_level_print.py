
from collections import deque

class Node:
    """Node structure """
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


def levelOrder(root):

    if not root:
        return

    queue = deque([])
    queue.append(root)
    queue.append(None)
    while queue:
        temp = queue.popleft()
        if temp == None:
            print()
            if queue:
                queue.append(None)

        else:

            print(temp.data, end = " ")

            if temp.left:
                queue.append(temp.left)

            if temp.right:
                queue.append(temp.right)


if __name__ == '__main__':
    root = Node(8)
    root.left = Node(10)
    root.right = Node(3)
    root.left.left = Node(1)
    root.left.right = Node(6)
    root.left.right.left = Node(9)
    root.left.right.right = Node(7)
    root.right.right = Node(14)
    root.right.right.left = Node(13)


    levelOrder(root)
