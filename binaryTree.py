from re import search


class BinaryTree:
    def __init__(self, data, parent=None):
        self.data = data
        self.left = None
        self.right = None
        self.parent = parent

    def addNode(self, data):
        if data == self.data:
            return

        if self.data > data:
            if self.left:
                self.left.addNode(data)
            else:

                self.left = BinaryTree(data, self)

        else:
            if self.right:
                self.right.addNode(data)
            else:
                self.right = BinaryTree(data, self)

    def getLevel(self):
        counter = 0
        while self.parent:
            counter += 1
            self = self.parent
        return counter

    def printTree(self):
        decoration = ' ' * self.getLevel() + '--|' if self.parent else " "
        print(decoration + str(self.data))
        if self.left:
            self.left.printTree()
        if self.right:
            self.right.printTree()

    def inOrderTraversal(self):
        elements = []
        if self.left:
            elements += self.left.inOrderTraversal()
        elements.append(self.data)
        if self.right:
            elements += self.right.inOrderTraversal()
        return elements

    def listToTree(self, data: list):
        for i in data:
            self.addNode(i)

    def search(self, data):
        if self.data == data:
            return self
        elif data< self.data:
            if self.left:
              return  self.left.search(data)
            else:
                return False
        else:
            if self.right:
              return  self.right.search(data)
            else:
                return False


if __name__ == '__main__':
    Root = BinaryTree(20)

    Root.listToTree([20, 10, 40, 50, 30, 5, 15])
    Root.printTree()
    print(Root.inOrderTraversal())
    x=10
    print(Root.search(x) )
