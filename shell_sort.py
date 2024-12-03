# Shell sort is an optimization over insertion sort
# when small elements are towars the end it takes many, comparisons and swaps

"""
1. Start with gap = n/2 and sort sub arrays
2. keep reducing gap by n/2 and keep on sorting subarrays
3. Last iteration should have gap = 1. At this point it is same as insertion sort 
Worst-case performance is O(n^2) - worst known for worst case gap sequence
                          O(n log^2 n) - best known for worst case gap sequence
Best-case performance is O(n log n) - most gap sequences
                         O(n log^2 n) - best known worst case gap sequences

"""

def shell_sort(arr):
    size = len(arr)
    gap = size // 2

    while gap > 0:
        for i in range(gap, size):
            anchor = arr[i]
            j = i
            while j >= gap and arr[j-gap] > anchor:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = anchor
        gap = gap // 2 

if __name__ == '__main__':
    elements = [21, 38, 29, 17, 4, 25, 11, 32, 9]
    shell_sort(elements)
    print(elements)

    tests = [
        [89, 78, 61, 53, 23, 21, 17, 12, 9, 7, 6, 2, 1],
        [],
        [1,5,8,9],
        [234,3,1,56,34,12,9,12,1300],
        [5]
    ]
    
    for elements in tests:
        shell_sort(elements)
        print(elements)