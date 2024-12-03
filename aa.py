class Node():
    def __init__(self, data):
        self.right = None
        self.data = data
        self.left = None
    
    def add(self, data):
        if self.data == data:
            return 
        
        if data < self.data:
            if self.left:
                self.left.add(data)
            else:
                self.left = Node(data)
        else:
            if self.right:
                self.right.add(data)
            else:
                self.right = Node(data)
    
    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data, end="->")
        if self.right:
            self.right.print_tree()

    def printf(self):
        print(self.data)

    def search(self, data):
        if data == self.data:
            return True
        
        if data < self.data:
            if self.left:
                return self.left.search(data)
            else:
                return False
        else:
            if self.right:
                return self.right.search(data)
            else:
                return False
        
    def inorder(self):
        ele = [ ]
        if self.left:
            ele += self.left.inorder()
        ele.append(self.data)
        if self.right:
            ele += self.right.inorder()
        return ele
    
    def preorder(self):
        ele = []
        ele.append(self.data)
        if self.left:
            ele += self.left.preorder()
        if self.right:
            ele += self.right.preorder()
        return ele

    def postorder(self):
        ele = []
        if self.left:
            ele += self.left.postorder()
        if self.right:
            ele += self.right.postorder()
        ele.append(self.data)
        return ele

    def delete(self, data):
        if data < self.data:
            if self.left:
                self.left = self.left.delete(data)
        elif data > self.data:
            if self.right:
                self.right = self.right.delete(data)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            
            min_val = self.right.mini()
            self.data = min_val
            self.right = self.right.delete(min_val)

        return self


    def mini(self):
        if self.left is None:
            return self.data
        return self.left.mini()
    
    def maxi(self):
        if self.right is None:
            return self.data
        return self.right.maxi()
    
    def find(self, n):
        if n == self.data or self is None:
            return self
        if n < self.data:
            if self.left:
                return self.left.find(n)
            else:
                return None
        else:
            if self.right:
                return self.right.find(n)
            else:
                return None
            
    def traverse_to_leaf(self):
        if self is None:
            return None
        path = [ ]
        current = self
        while current is not None:
            path.append(current.data)
            if current.left is None and current.right is None:
                break
            if current.left is not None:
                current = current.left
            else:
                current = current.right
        return path
    
    def height(self):
        if self is None:
            return -1  
        left_height = self.left.height() if self.left else -1
        right_height = self.right.height() if self.right else -1
        return 1 + max(left_height, right_height)
    
    def kth_large(self, k):
        if self is None:
            return None
        
        stack = [ ]
        current = self

        while True:
            while current:
                stack.append(current)
                current = current.right

            current = stack.pop()
            k -= 1
            if k == 0:
                return current.data
            current = current.left
            
    def reverse_inorder(self):
        if self is None:
            return 
        
        ele = [ ]
        if self.right:
            ele += self.right.reverse_inorder()
        ele.append(self.data)
        if self.left:
            ele += self.left.reverse_inorder()
        
        return ele
        

def Build_tree(numbers):
    root = Node(numbers[0])

    for i in range(1, len(numbers)):
        root.add(numbers[i])
    
    return root

class Graph():
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        for start, end in edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
        
    def printgh(self):
        print(self.graph_dict)

    def short_path(self, start, end, path=[]):
        path = path + [start]

        if start == end:
            return path
        
        if start not in self.graph_dict:
            return None

        shortest_path = None
        for node in self.graph_dict[start]:
            if node not in path:
                sp = self.short_path(node, end, path)
                if sp:
                    if shortest_path is None or len(sp) < len(shortest_path):
                        shortest_path = sp
        
        return shortest_path


if __name__ == "__main__":
    numbers = [12,4,6,8,13,27,15]
    Tree = Build_tree(numbers)
    Tree.print_tree()
    Tree.printf()
    print(Tree.search(8))
    print(Tree.inorder())
    print(Tree.preorder())
    print(Tree.postorder())

    start_node = Tree.find(4)
    if start_node is None:
        print("The node not found")
    else:
        path_node = start_node.traverse_to_leaf()
        if len(path_node) == 1:
            print(f"The node is a leaf:{path_node}")
        else:
            print(f"The node is not a leaf:{path_node}")
        
    print(Tree.height())
    print(Tree.kth_large(4))
    kth = Tree.reverse_inorder()
    print(kth[3])
    print(Tree.reverse_inorder())
    

   
    """ routes = [ ("a","b"), ("a","d"), ("b","c"),("c","d"),("c","e"),("d","f") ]
    routes_gh = Graph(routes)
    routes_gh.printgh()
    print(routes_gh.short_path("a","e")) """
