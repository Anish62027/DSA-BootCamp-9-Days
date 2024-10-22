class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key


class BinarySearchTree:
    def __init__(self):
        self.root = None

    
    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, root, key):
        if key < root.value:
            if root.left is None:
                root.left = Node(key)
            else:
                self._insert(root.left, key)
        else:
            if root.right is None:
                root.right = Node(key)
            else:
                self._insert(root.right, key)

   
    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, root, key):
        if root is None:
            return root
        if key < root.value:
            root.left = self._delete(root.left, key)
        elif key > root.value:
            root.right = self._delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            temp = self._minValueNode(root.right)
            root.value = temp.value
            root.right = self._delete(root.right, temp.value)

        return root

    def _minValueNode(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    # 3. Traversals in the BST
    # Inorder Traversal
    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, root, result):
        if root:
            self._inorder(root.left, result)
            result.append(root.value)
            self._inorder(root.right, result)

    # Preorder Traversal
    def preorder(self):
        result = []
        self._preorder(self.root, result)
        return result

    def _preorder(self, root, result):
        if root:
            result.append(root.value)
            self._preorder(root.left, result)
            self._preorder(root.right, result)

    # Postorder Traversal
    def postorder(self):
        result = []
        self._postorder(self.root, result)
        return result

    def _postorder(self, root, result):
        if root:
            self._postorder(root.left, result)
            self._postorder(root.right, result)
            result.append(root.value)

    
    def search(self, key):
        return self._search_bst(self.root, key)
    
    def _search_bst(self, node, key):
        if node is None or node.value == key:  
            return node
        if key < node.value:
            return self._search_bst(node.left, key)
        else:
            return self._search_bst(node.right, key)

   
    def get_root(self):
        return self.root



bst = BinarySearchTree()

while True:
    choice = int(input('''\nEnter a Number:
        1. Insert
        2. Search
        3. Display In-order Traversal
        4. Display Pre-order Traversal
        5. Display Post-order Traversal
        6. Get Root
        7. Exit
        
        Enter Your Choice: '''))

    if choice == 1:
        key = int(input("Enter the value to insert: "))
        bst.insert(key)
        print(f"Inserted {key} into the BST.")
    
    elif choice == 2:
        search_key = int(input("Enter the value to search: "))
        result = bst.search(search_key)
        if result:
            print(f"Key {search_key} found in BST.")
        else:
            print(f"Key {search_key} not found in BST.")

    elif choice == 3:
        traversal_result = bst.inorder()
        print("In-order Traversal:", traversal_result)

    elif choice == 4:
        traversal_result = bst.preorder()
        print("Pre-order Traversal:", traversal_result)

    elif choice == 5:
        traversal_result = bst.postorder()
        print("Post-order Traversal:", traversal_result)

    elif choice == 6:  
        root = bst.get_root()
        if root:
            print(f"The root of the BST is: {root.value}")
        else:
            print("The tree is empty, no root exists.")

    elif choice == 7:
        print("Exiting...")
        break

    else:
        print("Invalid Choice. Please enter a number between 1 and 7.")
