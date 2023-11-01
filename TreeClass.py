class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def reverseTree(root):
    if root is None:
        return None

    #swap subtrees
    root.left, root.right = root.right, root.left

    reverseTree(root.left)
    reverseTree(root.right)

    return root

def printTree(root):
    if(root):
        print(root.value, end=" ")
        printTree(root.left)
        printTree(root.right)
