#Buatlah Doubly Linked List yang menyimpan sebuah rute. Rute yang dimaksud adalah nama-nama jalan yang anda lalui dari tempat tinggal anda menuju Tugu Jogja (dengan asumsi rute berangkat = rute pulang). Tampilkan rute keberangkatan anda dan rute kepulangan menggunakan operasi dasar Doubly Linked List yang sudah anda pelajari.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def tambah(self, data):
        nodeBaru = Node(data)
        if self.head is None:
            self.head = nodeBaru
        else:
            now = self.head
            while now.next:
                now = now.next
            now.next = nodeBaru
            nodeBaru.prev = now

    def tampilMaju(self):
        now = self.head
        while now:
            print(now.data)
            now = now.next

    def tampilMundur(self):
        now = self.head
        while now.next:
            now = now.next
        while now:
            print(now.data)
            now = now.prev

ruteList = DoublyLinkedList()

ruteList.tambah("Jl. Suropati")
ruteList.tambah("Jl. Sinduadi Jetis")
ruteList.tambah("Jl. Selokan Mataram")
ruteList.tambah("Jl. Magelang")
ruteList.tambah("Jl. Pangeran Diponegoro")

print("Rute Berangkat: ")
ruteList.tampilMaju()
# ruteList.tambah("Jl. A")

print("Rute Pulang:")
ruteList.tampilMundur()