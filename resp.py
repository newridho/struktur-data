#1 Buatlah program untuk menambahkan elemen pada ke dalam Doubly Linked List pada posisi tertentu sesuai keinginan pengguna(index buatan programmer)
#2 Buatlah program untuk menghapus elemen pada Doubly Linked List pada posisi tertentu sesuai keinginan pengguna(index buatan programmer)

class Node:
    def __init__(self, barang, harga):
        self.barang = barang
        self.harga = harga
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self, barang, harga):
        self.head = None
        self.tail = None
        self.length = 1

    def append(self, barang, harga, position):
        new_node = Node(barang, harga)

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

    def pop(self):
        if self.length == 0:
            return None
        current = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            current.prev = None
        self.length -= 1
        return current

    def display(self):
        current = self.head
        while current:
            print(current.barang, current.harga)
            current = current.next

dll = DoublyLinkedList("Telurr", 1200)
print("BARANG | HARGA")
dll.append("Telur", 1000, 1)  
dll.append("Sabun", 200, 2)  
dll.append("Shampo", 250, 3)  
dll.append("Handuk", 3000, 4)  
dll.append("Odol", 1200, 5)  
print(dll.pop())
dll.display()  
# dll.pop(2)