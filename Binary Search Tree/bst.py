class Node: #Готово
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:#Готово
    def __init__(self):
        self.root = None
        self.visited_count = 0

    def insert(self, value): #Много ещё делать
        if self.root is None:
            self.root = Node(value)
        else:
            current = self.root
            while True:
                if value < current.value:
                    if current.left is None:
                        current.left = Node(value)
                        break
                    current = current.left
                else:
                    if current.right is None:
                        current.right = Node(value)
                        break
                    current = current.right

    def fromArray(self, array):#Сделано
        for i in array:
            self.insert(i)

    def search(self, value):#Ждём саню
        self.visited_count = 0
        current = self.root
        while current is not None:
            self.visited_count += 1
            if value == current.value:
                return True
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        return False

    def min(self):#while тупо иду на лево к самому маленькому значению(взять с гпт, у всех одинаково)
        self.visited_count = 0
        current = self.root
        if not current:
            return None
        while current.left:
            self.visited_count += 1
            current = current.left
        self.visited_count += 1
        return current.value

    def max(self):#while тупо иду на право к самому большому значению
        self.visited_count = 0
        current = self.root
        if not current:
            return None
        while current.right:
            self.visited_count += 1
            current = current.right
        self.visited_count += 1
        return current.value
    def visitedNodes(self):#Ждём саню
        return self.visited_count