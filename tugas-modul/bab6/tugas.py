#Berdasarkan hasil implementasi yang sudah Anda lakukan sebelumnya, buatlah implementasi kode program menggunakan bahasa pemrograman Python untuk skenario berikut:
#1. Buat Linked List dengan satu elemen = "saya".
#2. Append-kan node baru = "adalah".
#3. Insert-kan node baru = "nama masing-masing" ke index = 2
#4. Prepend-kan node baru = "nama"
#5. Tampilkan seluruh elemen Linked List.
#6. Ubah "nama masing-masing" menjadi nama teman anda.

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert(self, data, index):
        new_node = Node(data)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            for _ in range(index - 1):
                if current.next is None:
                    raise IndexError("Index out of range")
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def change_name(self, index, new_name):
        current = self.head
        for _ in range(index):
            if current is None:
                raise IndexError("Index out of range")
            current = current.next
        current.data = new_name

# 1. Create a Linked List with one element = "me".
linked_list = LinkedList()
linked_list.append("Saya")

# 2. Add a new node = "is".
linked_list.append("adalah")

# 3. Insert new node = "respective name" to index = 2
linked_list.insert("respective name", 2)

# 4. Prepend new node = "name"
linked_list.prepend("Nama")

# 5. Display all Linked List elements.
linked_list.display()

# 6. Change "each other's name" to your friend's name.
linked_list.change_name(2, "friend's name")

        
