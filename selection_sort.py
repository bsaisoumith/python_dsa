# Big O complexity Time complexity = O(n^2) (all the cases)
# Space complexity = O(1)

""" def find_min_element(arr):
    min = 100000
    for i in range(len(arr)):
        if arr[i] < min:
            min = arr[i]
    return min """

def selection_sort(arr):
    size = len(arr)
    for i in range(size-1):
        min_index = i
        for j in range(min_index+1, size):
            if arr[j] < arr[min_index]:
                min_index = j
        if i != min_index:
            arr[i], arr[min_index] = arr[min_index], arr[i]   #swapping

def multilevel_selection_sort(elements, sort_by_list):
    for sort_by in sort_by_list[-1::-1]:
        for x in range(len(elements)):
            mid_index = x
            for y in range(x,len(elements)):
                if elements[y][sort_by] < elements[mid_index][sort_by]:
                    mid_index = y
            if x != mid_index:
                elements[x], elements[mid_index] = elements[mid_index], elements[x]
    

if __name__ == '__main__':
    elements = [78, 12, 15, 8 ,61, 53, 23, 27]
    selection_sort(elements)
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
        selection_sort(elements)
        print(f'sorted array: {elements}')

    elements = [
        {'First Name': 'Raj', 'Last Name': 'Nayyar'},
        {'First Name': 'Suraj', 'Last Name': 'Sharma'},
        {'First Name': 'Karan', 'Last Name': 'Kumar'},
        {'First Name': 'Jade', 'Last Name': 'Canary'},
        {'First Name': 'Raj', 'Last Name': 'Thakur'},
        {'First Name': 'Raj', 'Last Name': 'Sharma'},
        {'First Name': 'Kiran', 'Last Name': 'Kamla'},
        {'First Name': 'Armaan', 'Last Name': 'Kumar'},
        {'First Name': 'Jaya', 'Last Name': 'Sharma'},
        {'First Name': 'Ingrid', 'Last Name': 'Galore'},
        {'First Name': 'Jaya', 'Last Name': 'Seth'},
        {'First Name': 'Armaan', 'Last Name': 'Dadra'},
        {'First Name': 'Ingrid', 'Last Name': 'Maverick'},
        {'First Name': 'Aahana', 'Last Name': 'Arora'}
    ]

    print(f'Given unsorted array:',*elements,sep = '\n')
    multilevel_selection_sort(elements,['First Name','Last Name'])
    print(f'Array after Multi-level sorting:', *elements, sep = '\n')



    