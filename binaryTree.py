from re import search
from xml.dom.minidom import Element


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

    def preOrderTraversal(self):
        element = []
        element.append(self.data)
        if self.left:
            element += self.left.preOrderTraversal()
        if self.right:
            element += self.right.preOrderTraversal()
        return element

    def postOrderTraversal(self):
        element = []
        if self.left:
            element += self.left.postOrderTraversal()
        if self.right:
            element += self.right.postOrderTraversal()
        element.append( self.data)
        return element

    def listToTree(self, data: list):
        for i in data:
            self.addNode(i)

    def search(self, data):
        if self.data == data:
            return True
        elif data < self.data:
            if self.left:
                return self.left.search(data)
            else:
                return False
        else:
            if self.right:
                return self.right.search(data)
            else:
                return False

    def findMin(self):
        while self.left:
            self = self.left
        return self.data

    def findMax(self):
        while self.right:
            self = self.right
        return self.data

    def totalSum(self):
        sum = 0
        if self.left:
            sum += self.left.totalSum()
        sum += self.data
        if self.right:
            sum += self.right.totalSum()
        return sum


if __name__ == '__main__':
    Root = BinaryTree(20)

    Root.listToTree([20, 10, 40, 23, 54, 34, 23, 56, 34,
                    0, -12, 24, 5, 3, 50, 30, 5, 15])
    Root.printTree()
    print(Root.inOrderTraversal())
    print(Root.postOrderTraversal())
    print(Root.preOrderTraversal())
    x = 245
    print(Root.search(x))
    print(Root.findMax())
    print(Root.findMin())
    print(Root.totalSum())
