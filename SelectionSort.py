# selection sort

def SelectionSort(list):
    for i in range(len(list)-1):
        minpos = i
        for j in range(i, len(list)):
            if list[j] < list[minpos]:
                minpos = j
        temp = list[i]
        list[i] = list[minpos]
        list[minpos] = temp

list = [5, 3, 8, 6, 7, 2, 9, 0, 1, 4]

SelectionSort(list)

print('My sorted list is ', list)
