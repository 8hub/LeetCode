class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root: TreeNode) -> str:
        def serialize_node(node):
            if node is None:
                return 'n,'
            return str(node.val) + ',' + serialize_node(node.left) + serialize_node(node.right)

        return serialize_node(root)


    def deserialize(self, data: str) -> TreeNode:
        def helper(data_list):
            val = data_list.pop(0)  # get the first element
            if val == 'n':  # if the first element is 'n', it's a null node
                return None

            # create a new TreeNode with the first element
            node = TreeNode(int(val))

            node.left = helper(data_list)  # recursively build the left subtree
            node.right = helper(data_list)  # recursively build the right subtree

            return node

        data_list = data.split(',')  # split the string by commas
        return helper(data_list)


test_tree = TreeNode(1)
test_tree.left = TreeNode(2)
test_tree.right = TreeNode(3)
test_tree.left.left = TreeNode(4)
test_tree.left.right = TreeNode(5)
test_tree.left.right.left = TreeNode(6)

test = Codec()
print(test.serialize(test_tree))
print(test.deserialize(test.serialize(test_tree)))
