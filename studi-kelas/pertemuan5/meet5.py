#Berdasarkan hasil implementasi yang sudah Anda lakukan sebelumnya, buatlah implementasi kode program menggunakan bahasa pemrograman Python untuk skenario berikut:
#1. Buat Linked List dengan satu elemen = "saya".
#2. Append-kan node baru = "adalah".
#3. Insert-kan node baru = "nama masing-masing" ke index = 2
#4. Prepend-kan node baru = "nama"
#5. Tampilkan seluruh elemen Linked List.
#6. Ubah "nama masing-masing" menjadi nama teman anda.

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def insert(self, value, index):
        if index == 0:
            self.prepend(value)
        else:
            new_node = Node(value)
            current = self.head
            for _ in range(index - 1):
                if current.next:
                    current = current.next
                else:
                    raise IndexError("Index out of range")
            new_node.next = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.value, end="-> ")
            current = current.next
        print("None")

    def change_name(self, index, new_name):
        current = self.head
        for _ in range(index):
            if current.next:
                current = current.next
            else:
                raise IndexError("Index out of range")
        current.value = new_name

linked_list = LinkedList()
linked_list.append("Saya")

linked_list.append("adalah")

linked_list.insert("nama masing-masing", 2)

linked_list.prepend("Nama")

linked_list.change_name(3, "Munif")

linked_list.display()

        
