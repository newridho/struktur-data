#1 Buatlah program untuk menambahkan elemen pada ke dalam Doubly Linked List pada posisi tertentu sesuai keinginan pengguna(index buatan programmer)
#2 Buatlah program untuk menghapus elemen pada Doubly Linked List pada posisi tertentu sesuai keinginan pengguna(index buatan programmer)

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def add_at_position(self, data, position):
        new_node = Node(data)

        if position == 1:
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
        else:
            current = self.head
            for _ in range(position - 2):
                if current is None:
                    print("Invalid position")
                    return
                current = current.next

            if current is None:
                print("Invalid position")
                return

            new_node.next = current.next
            new_node.prev = current
            if current.next:
                current.next.prev = new_node
            current.next = new_node

    def delete_at_position(self, position):
        if self.head is None:
            print("List is empty")
            return

        if position == 1:
            if self.head.next:
                self.head.next.prev = None
            self.head = self.head.next
        else:
            current = self.head
            for _ in range(position - 2):
                if current is None:
                    print("Invalid position")
                    return
                current = current.next

            if current is None or current.next is None:
                print("Invalid position")
                return

            next_node = current.next.next
            if next_node:
                next_node.prev = current
            current.next = next_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end="-> ")
            current = current.next
        print("None")

dll = DoublyLinkedList()
dll.add_at_position(9, 1)  
dll.add_at_position(8, 2)  
dll.add_at_position(7, 3)  
dll.display()  

dll.delete_at_position(2)  
dll.display()  