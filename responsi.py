class Node:
    def __init__(self, barang, harga):
        self.barang = barang
        self.harga = harga
        self.next = None

class LinkedList:
    def __init__(self, barang, harga):
        new_node  = Node(barang, harga)
        self.head = None
        self.tail = None
        self.length = 1

    def append(self, barang, harga):
        new_node = Node(barang, harga)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while temp.next is not None:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def display(self):
        temp = self.head
        while temp is not None:
            print("Barang: ", temp.barang, "Harga: ", temp.harga)
            temp = temp.next

    
    
myLinkedList = LinkedList("Barang \t", "Harga")
while True:
    print("\nMenu")
    print("1. Tambah Barang ke keranjang")
    print("2. Lihat Barang")
    print("3. Hapus barang")
    print("4. Keluar menu")

    menu = input("Pilih Menu: ")
    if menu == '1':
        myLinkedList.append("telur", 1000)
    elif menu == '2':
        myLinkedList.display()
    elif menu == '3':
        print(myLinkedList.pop().harga.barang)
    elif menu == '4':
        print("Terima Kasih")
        exit()
    else:
        print("Menu Tidak Ada")
