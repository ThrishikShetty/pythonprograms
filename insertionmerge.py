def merge_sort(array):

    if len(array) > 1:
        mid = len(array) // 2
        left_half = array[:mid]
        right_half = array[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                array[k] = left_half[i]
                i += 1
            else:
                array[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            array[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            array[k] = right_half[j]
            j += 1
            k += 1

    return array





def insertion_sort(array):
    for i in range(1,len(array)):
        key = array[i]
        j=i-1
        while j>=0 and key<array[j]:
            array[j+1]=array[j]
            j=j-1
        array[j+1]=key
    print("Sorting using Insertion Sort")
    print(array)


while(True):
    print(" ")
    print("press 1 to sort elements using insertion sort")
    print("press 2 to sort elements using merge sort")
    print("press 3 exit")
    choice=input("enter your choice ")
    if(choice=='1'):
        array = []
        print("To sort the elements using insertion sort")
        n = int(input("enter the number of elements "))
        print("enter the list elements")
        for i in range(n):
            value = int(input())
            array.append(value)

        print("\nUnsorted List")
        print(array)
        insertion_sort(array)
    elif (choice == '2'):
        array = []
        print("To sort the elements using merge sort")
        n = int(input("enter the number of elements "))
        print("enter the list elements")
        for i in range(n):
            value = int(input())
            array.append(value)
        print("\nUnsorted List")
        print(array)
        print(merge_sort(array))
    elif( choice == 'x' or choice=='X' ):
        print("you have exited program")
        break
    else:
        print("Invalid Choice")
        break







