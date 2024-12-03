# worst case performance O(n^2) comparisons and swaps
# Best case perfomance O(n) comparisons and O(1) swaps
# Average performance O(n^2) comparisons and swaps
# Worst case space complexity is O(n) total, O(1) auxiliary

# Insertion sort is a simple sorting algorithm that builds the finl sorted array (or list) one item at a time

def insertion_sort(elements):
    for i in range(1, len(elements)):
        anchor = elements[i]
        j = i - 1
        while j >= 0 and anchor < elements[j]:
            elements[j+1] = elements[j]
            j = j - 1
        elements[j + 1] = anchor

def place_to_insert(array, key):
    index = 0
    for i in array:
        if i > key:
            break
        else:
            index += 1
    return index


def insert_to_sorted(array, key):
    index = place_to_insert(array, key)
    return array[0:index]+[key]+array[index:]

def insertionSortRec(arr, i , n):
    if i == n:
        return

    j = i

    while j > 0 and arr[j - 1] > arr[j]:
        arr[j], arr[j - 1] = arr[j - 1], arr[j]
        j -= 1

    insertionSortRec(arr, i + 1, n)

def insertionSort(arr, n):

   # Call the recursive function to perform the insertion sort.
   insertionSortRec(arr, 0, len(arr))


if __name__ == '__main__':
    elements = [11, 9, 29, 7, 2, 15, 28]
    #insertion_sort(elements)
    insertionSort(elements,len(elements))
    print(elements)


    array = [2, 1, 5, 7, 2, 0, 5]

    stream = []

    count = 0
    while(True):
        i = int(input())
        count += 1
        stream = insert_to_sorted(stream, i)
        if count % 2 == 1:
            print(f"Median of {stream} : {stream[(count)//2]}")
        else:
            i1 = count//2
            i2 = (count//2) - 1
            print(f"Median of {stream} : {(stream[i1] + stream[i2])/2}")
    



