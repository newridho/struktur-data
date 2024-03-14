#Diketahui suatu Linked List memiliki lima elemen dengan nilai seperti berikut: 23, 43, 12, 71, 87.
#buatlah sebuah fungsi untuk me-reverse setiap elemen di dalam Linked List, sehingga pada saat ditampilkan akan menghasilkan output sebagai berikut: 87, 71, 12, 43, 23.
#Anda tidak diperbolehkan menggunkan satu pun operasi dasar yang sudah dipelajari untuk me-reverse elemen di dalam Linked List.

class Node:
    def __init__(self, data=None):
        self.data = data
        self.lanjut = None

def reverseList(depan):
    if depan is None or depan.lanjut is None:
        return depan

    sisa = reverseList(depan.lanjut)
    depan.lanjut.lanjut = depan
    depan.lanjut = None

    return sisa

depan = Node(23)
depan.lanjut = Node(43)
depan.lanjut.lanjut = Node(12)
depan.lanjut.lanjut.lanjut = Node(71)
depan.lanjut.lanjut.lanjut.lanjut = Node(87)

depan = reverseList(depan)

saatIni = depan
while saatIni:
    print(saatIni.data, end=" ")
    saatIni = saatIni.lanjut