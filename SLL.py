# self represents the instance of the class. By using the “self”  we can access the attributes and methods of the class in python.
#  Self is always pointing to Current Object.

class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_last(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
        
        itr.next = Node(data, None)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_last(data)
        
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next

        return count
    
    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")
        
        if index ==  0:
            self.insert_at_begining(data)
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                break

            itr = itr.next
            count += 1
    
    
    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")
        
        if index == 0:
            self.head = self.head.next
            return 
        
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count += 1

    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            return

        if self.head.data == data_after:
            self.head.next = Node(data_to_insert,self.head.next)
            return

        itr = self.head
        while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert, itr.next)
                break

            itr = itr.next
        
    def remove_by_value(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next


    def print(self):
        if self.head is None:
            print("Linked List is empty")
            return
        
        itr = self.head
        llstr = ''

        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next
        
        print(llstr)
        
if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_begining(5)
    ll.insert_at_begining(89)
    ll.insert_at_last(65)
    ll.insert_at_last(23)
    ll.print() 
    print("Length:", ll.get_length())

    ll.remove_at(2)
    ll.print()

    ll.insert_values(["banana","mango","grapes","orange","apple"])
    ll.print()
    print("Length:", ll.get_length())

    ll.remove_at(3)
    # ll.remove_at(20)   # It throws an exception 
    # ll.remove_at(-1)
    ll.print()

    ll.insert_at(0,"figs")
    ll.insert_at(2,"jackfruit")
    ll.print()

    ll.insert_after_value("mango","kiwi")
    ll.print()
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.print() 
