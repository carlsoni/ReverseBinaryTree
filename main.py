from TreeClass import TreeNode, reverseTree, printTree

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print("Original Tree: \n")
printTree(root)

reverseRoot = reverseTree(root)
print("\nNew Tree: \n")
printTree(reverseRoot)




