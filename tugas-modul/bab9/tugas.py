#Buatlah method yang digunakan untuk menghapus suatu node di dalam Binary Search Tree dan menyeimbangkan struktur Binary Search Tree setelah operasi penghapusan node dari suatu Binary Search Tree. Beri nama method ini reconstruct()

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = Node(value)
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right
    
    def reconstruct(self, value):
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                break
        if temp is None:
            return False
        self.root = self.delete_node(self.root, value)
        return True
    
    def min_value_node(self, current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node
    
    def delete(self, value):
        return self.delete_node(self.root, value)
    
    def delete_node(self, current_node, value):
        if current_node is None:
            return current_node
        if value < current_node.value:
            current_node.left = self.delete_node(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self.delete_node(current_node.right, value)
        else:
            if current_node.left is None:
                temp = current_node.right
                current_node = None
                return temp
            elif current_node.right is None:
                temp = current_node.left
                current_node = None
                return temp
            temp = self.min_value_node(current_node.right)
            current_node.value = temp.value
            current_node.right = self.delete_node(current_node.right, temp.value)
        return current_node

    def inorder_traversal(self, start, traversal):
        if start:
            traversal = self.inorder_traversal(start.left, traversal)
            traversal += (str(start.value) + ' ')
            traversal = self.inorder_traversal(start.right, traversal)
        return traversal
    
    def display(self):
        print(self.inorder_traversal(self.root, ''))

# Driver code
bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(3)
bst.insert(7)

print("Sebelum rekonstruksi: ")
bst.display()
bst.reconstruct(5)
print("Setelah rekonstruksi: ")
bst.display()