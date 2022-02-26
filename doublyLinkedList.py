class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def addBeginning(self, data):
        if self.tail == None:
            node = Node(data)
            self.head = node
            self.tail = node
            return
        node = Node(data, self.head)
        self.head.prev = node
        self.head = node

    def addEnd(self, data):
        if self.tail == None:
            node = Node(data)
            self.head = node
            self.tail = node
            return
        node = Node(data, None, self.tail)
        self.tail.next = node
        self.tail = node

    def printForward(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

    def printBackward(self):
        node = self.tail
        while node:
            print(node.data)
            node = node.prev

    def listToLinkedList(self, List: list):
        self.head = None
        self.tail = None
        for i in List:
            self.addEnd(i)

    def length(self):
        node = self.head
        ctr = 0

        while node:
            ctr += 1
            node = node.next
        return ctr

    def inserAtIndex(self, index, data):
        if index < 0 or index >= self.length():
            raise Exception('Invalid index')

        if index == 0:
            nodex = Node(data, self.head)
            self.head.prev = nodex
            self.head = nodex
            return

        node = self.head
        for i in range(index):  # no need to minus one since we can use prev
            node = node.next
        nodeData = Node(data, node, node.prev)
        node.prev.next = nodeData
        return

    def removeAtIndex(self, index: int):
        if index < 0 or index >= self.length():
            raise Exception('Invalid index')

        if index == 0:
            self.head.next.prev = None
            self.head = self.head.next
            return

        node = self.head
        for i in range(index):
            node = node.next
        node.prev.next = node.next


list1 = LinkedList()
list1.addBeginning(5)
list1.addBeginning(4)
list1.addBeginning(55)
list1.addBeginning(45)
list1.addEnd(100)
list1.printBackward()
