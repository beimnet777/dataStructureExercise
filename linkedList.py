

class Node:
  def __init__(self,data,next=None):
      self.data=data
      self.next=next


class LinkedList:
  def __init__(self):
    self.head=None


  def addBeginning(self,data):
    self.head=Node(data,self.head)


  def printList(self):
    node=self.head
    
    while node:
      print(node.data)
      node=node.next


  def addEnd(self,data):
    nodeEnd=Node(data)
    if self.head==None:
      self.head=nodeEnd
      return
    node=self.head
    while node.next:
      node=node.next
    node.next=nodeEnd


  def listToLinkedList(self,List:list):
    self.head=None
    for i in List:
      self.addEnd(i)


  def length(self):
    node=self.head
    ctr=0
    while node:
      ctr+=1
      node=node.next
    return ctr


  def insertAtIndex(self,index:int,data):
    if index>= self.length() or index<0:
      raise Exception("Invlaid index")
    if index==0:
      self.head=Node(data,self.head)
      return
    node=self.head
    for i in range(index-1):
      #get the previous and ser its next to a node crated having data and next 
      # value of the object at the given index 
      node=node.next
    Node1=Node(data,node.next)
    node.next=Node1
  def removeAtIndex(self,index:int):
    if index<0 or index>=self.length():
      raise Exception('Invalid index')
    if index==0:
      self.head=self.head.next
      return  
    node=self.head
    for i in range(index-1):
      node=node.next
    node.next=node.next.next
  def insertAfterValue(self,data,value):
    node = self.head
    while node:
      if node.data==value:
        node.next=Node(data,node.next)
        return
      node=node.next
    raise Exception('Value not found')
  def removeByValue(self,value):
    node=self.head
    if node.data==value:
      self.head=node.next
    while node:
      if node.next.data==value:
        node.next=node.next.next
        return
      node=node.next
    raise Exception('Value not found')





if __name__=='__main__':
  list1=LinkedList()
  # list1.addBeginning(5)
  # list1.addBeginning(4)
  # list1.addBeginning(55)
  # list1.addBeginning(45)
  # list1.addEnd(100)
  list1.listToLinkedList([12,4,345,2,31,1])
  list1.insertAtIndex(0,3423)
  list1.removeAtIndex(2)
  list1.insertAfterValue(43,2)
  list1.removeByValue(2)
  list1.printList()
