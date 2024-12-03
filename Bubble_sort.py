# Time complexity is O(n^2) and space complexity is O(1)

def bubble_sort(elements):
    size = len(elements)

    for k in range(size - 1):       # size - 1 for every iteration largest element in the list will be at the last
        for i in range(size-1-k):   # size - 1 - k becoz no need to compare with the larger elements at the end of the list
            if elements[i] > elements[i+1]:
                elements[i], elements[i+1] = elements[i+1], elements[i]

def bubble_sort_1(elements, key):
    size = len(elements)

    for i in range(size - 1):
        for j in range(size - i - 1):
            if elements[j][key] > elements[j+1][key]:
                elements[j], elements[j+1] = elements[j+1], elements[j] 

def bubble_sort_recursive(elements,n):
    if n <= 1:
        return
    
    for i in range(n - 1):
        if elements[i] > elements[i + 1]:
            elements[i], elements[i + 1] = elements[i + 1], elements[i]  # Swap elements if they are in the wrong order
    
    bubble_sort_recursive(elements, n - 1)


if __name__ == '__main__':
    elements = [5,9,2,1,67,34,88,34]

    bubble_sort(elements)
    print(elements)

    tests = [
        [11,9,29,7,2,15,28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6]
    ]

    for elements in tests:
        bubble_sort(elements)
        print(f'sorted array: {elements}')

    elements = [
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
    ]

    print("Before Sorting:",*elements, sep = '\n')
    bubble_sort_1(elements, key='transaction_amount')
    print("After Sorting:",*elements, sep = '\n')
    bubble_sort_1(elements, key='name')
    print("After Sorting:",*elements, sep = '\n')


