class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        inserted = False
        node = self.root
        while not inserted:
            if (new_val > node.value):
                if(node.right):
                    node = node.right
                else:
                    inserted = True
                    node.right = Node(new_val)
            elif(new_val < node.value):
                if(node.left):
                    node = node.left
                else:
                    inserted = True
                    node.left = Node(new_val)

    def search(self, find_val):
        node = self.root
        found = False
        while not found:
            if(find_val == node.value):
                found = True
                break
            elif(find_val > node.value):
                if(node.right):
                    node = node.right
                else:
                    break
            elif(find_val < node.value):
                if(node.left):
                    node = node.left
                else:
                    break
        return found

    def print_tree(self):
        return self.preorder_print(self.root, "")[:-1]

    def preorder_print(self, start, traversal):
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal
# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

print(tree.print_tree())

# Check search
# Should be True
print(tree.search(4))
# Should be False
print(tree.search(6))
