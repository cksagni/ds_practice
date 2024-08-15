

class Node:

    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def create_tree():
    node1 = Node(5, None, None)
    node2 = Node(6, node1, None)
    node3 = Node(7, node2, None)

    node4 = Node(8, None, None)
    node5 = Node(9, node4, None)
    node6 = Node(10, node5, None)
    node7 = Node(11, None, node6)

    root = Node(11, node3, node6)
    return root


def tree_h(root):
    if root is None:
        return 0
    height = 1 + max(tree_h(root.left), tree_h(root.right))
    return height


if __name__ == "__main__":
    root1 = create_tree()
    print(tree_h(root1))


