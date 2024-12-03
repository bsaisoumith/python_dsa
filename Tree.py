class TreeNode:
    def __init__(self,date):
        self.data = date
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level
    
    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else "" 
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()


def build_product_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("MAC"))
    laptop.add_child(TreeNode("Surface"))
    laptop.add_child(TreeNode("Thinkpad"))

    cellphone = TreeNode("Cell Phone")
    cellphone.add_child(TreeNode("iphone"))
    cellphone.add_child(TreeNode("Google Pixel"))
    cellphone.add_child(TreeNode("Redmi"))

    tv = TreeNode("TV")
    tv.add_child(TreeNode('Samsung'))
    tv.add_child(TreeNode("LG"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    return root


def location_tree():
    root = TreeNode("Global")

    India = TreeNode("India")

    Gujarat = TreeNode("Gujarat")
    Gujarat.add_child(TreeNode("Ahmedabad"))
    Gujarat.add_child(TreeNode("Baroda"))
    Karnataka = TreeNode("Karnataka")
    Karnataka.add_child(TreeNode("Bangluru"))
    Karnataka.add_child(TreeNode("Mysore"))

    USA = TreeNode("USA")

    New_Jersey = TreeNode("NEW JERSEY")
    New_Jersey.add_child(TreeNode("Princeton"))
    New_Jersey.add_child(TreeNode("Trenton"))
    Califonia = TreeNode("California")
    Califonia.add_child(TreeNode("San Francisco"))
    Califonia.add_child(TreeNode("Mountain View"))
    Califonia.add_child(TreeNode("Palo Alto"))

    root.add_child(India)
    root.add_child(USA)
    India.add_child(Gujarat)
    India.add_child(Karnataka)
    USA.add_child(New_Jersey)
    USA.add_child(Califonia)

    return root

def management():
    root = TreeNode("Nilupul")

    Chinmay = TreeNode("Chinmay (CTO)")
    Gels = TreeNode("Gels (HR Head)")

    root.add_child(Chinmay)
    root.add_child(Gels)

    Vishwa = TreeNode("Vishwa (Infrastructure Head)")
    Vishwa.add_child(TreeNode("Dhaval (Cloud Manager)"))
    Vishwa.add_child(TreeNode("Abhijit (App Manager)"))

    Chinmay.add_child(Vishwa)
    Chinmay.add_child(TreeNode("Aamir (Application Head)"))

    Gels.add_child(TreeNode("Peter (Recruitment Manager)"))
    Gels.add_child(TreeNode("Waqas (Policy Manager)"))

    return root

if __name__ == '__main__':
    root = build_product_tree()
    root.print_tree()

    root = location_tree()
    root.print_tree()
    
    root = management()
    root.print_tree()


