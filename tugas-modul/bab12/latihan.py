#Bubble Sort
def descend_bubble_sort(my_List):
    for i in range(len(my_List) - 1 , 0 , -1):
        for j in range(i):
            if my_List[j] < my_List[j + 1]:
                temp = my_List[j]
                my_List[j] = my_List[j + 1]
                my_List[j + 1] = temp

    return my_List

def ascend_bubble_sort(my_List):
    for i in range(len(my_List) - 1 , 0 , -1):
        for j in range(i):
            if my_List[j] > my_List[j + 1]:
                temp = my_List[j]
                my_List[j] = my_List[j + 1]
                my_List[j + 1] = temp

    return my_List

#Selection Sort
def descend_selection_sort(my_List):
    for i in range(len(my_List)):
        min_index = i
        for j in range(i+1, len(my_List)):
            if my_List[j] > my_List[min_index]:
                min_index = j
        my_List[i], my_List[min_index] = my_List[min_index], my_List[i]
    return my_List

def ascend_selection_sort(my_List):
    for i in range(len(my_List)):
        min_index = i
        for j in range(i+1, len(my_List)):
            if my_List[j] < my_List[min_index]:
                min_index = j
        my_List[i], my_List[min_index] = my_List[min_index], my_List[i]
    return my_List

list_angka = [4,2,6,5,1,3]
print("====Bubble Sort====")
print("Descending")
print("Sebelum di sorting : ", list_angka)
print("Setelah di sorting : ", descend_bubble_sort(list_angka))

print("Ascending")
print("Sebelum di sorting : ", list_angka)
print("Setelah di sorting : ", ascend_bubble_sort(list_angka))

print("\n====Selection Sort====")
print("Descending")
print("Sebelum di sorting : ", list_angka)
print("Setelah di sorting : ", descend_selection_sort(list_angka))

print("Ascending")
print("Sebelum di sorting : ", list_angka)
print("Setelah di sorting : ", ascend_selection_sort(list_angka))