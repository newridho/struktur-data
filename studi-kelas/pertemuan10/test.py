def bubble_sort(my_List):
    for i in range(len(my_List) - 1 , 0 , -1):
        for j in range(i):
            if my_List[j] > my_List[j + 1]:
                temp = my_List[j]
                my_List[j] = my_List[j + 1]
                my_List[j + 1] = temp

    return my_List

list_angka = [4,2,6,5,1,3]
print("Sebelum di sorting : ", list_angka)
print("Setelah di sorting : ", bubble_sort(list_angka))