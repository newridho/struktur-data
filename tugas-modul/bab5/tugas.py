#1. Lakukan riset di internet untuk menjelaskan secara singkat (berikan pula contohnya) apa yang dimaksud dengan immutable dan mutable pada bahasa Python!
# 2. Lakukan eksperimen yang sama seperti pada bagian pointer di modul ini untuk mengamati tipe data list, tuple, dan set!

#1 Riset : 
#Immutable adalah tipe data yang tidak dapat diubah setelah dideklarasikan. Contoh tipe data immutable adalah int, float, str, tuple, dan frozenset.
#Mutable adalah tipe data yang dapat diubah setelah dideklarasikan. Contoh tipe data mutable adalah list, set, dict, dan bytearray.

#2 Eksperimen :
#List
print("------List------")
list1 = [1, 2, 3, 4, 5]
list2 = list1
print("\nNilai Sebelum diupdate :")
print("List1 : ", list1)
print("List2 : ", list2)

print("\nNilai Sesudah diupdate :")
list1[2] = 10
print("List1 : ", list1)
print("List2 : ", list2)

#Tuple
print("\n------Tuple------")
tuple1 = (1, 2, 3, 4, 5)
tuple2 = tuple1
print("\nNilai Sebelum diupdate :")
print("Tuple1 : ", tuple1)
print("Tuple2 : ", tuple2)

print("\nNilai Sesudah diupdate :")
tuple2 = (6, 7, 8, 9, 10)
print("Tuple1 : ", tuple1)
print("Tuple2 : ", tuple2)

#Set
print("\n------Set------")
set1 = {1, 2, 3, 4, 5}
set2 = set1
print("\nNilai Sebelum diupdate :")
print("Set1 : ", set1)
print("Set2 : ", set2)

print("\nNilai Sesudah diupdate :")
set1.add(6)
print("Set1 : ", set1)
print("Set2 : ", set2)