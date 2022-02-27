class BinaryTree:
  def __init__ (self,data,parent=None):
    self.data=data
    self.left=None
    self.right=None
    self.parent=parent
  def addNode(self,data):
    if data==self.data:
      return
      
    if self.data>data: 
        if self.left:
          self.left.addNode(data) 
        else:  
            
          self.left=BinaryTree(data,self)
          

    else:
      if self.right:
        self.right.addNode(data) 
      else:
        self.right=BinaryTree(data,self)
  def getLevel(self):
    counter=0
    while self.parent:
      counter+=1
      self=self.parent
    return counter    
  def printTree(self):
    decoration=' '* self.getLevel() + '--|' if self.parent else " "
    print(decoration+ str(self.data))
    if  self.left:
      self.left.printTree()
    if self.right:
      self.right.printTree()
  def listToTree(self,data:list):
    for i in data:
      self.addNode(i)

if __name__=='__main__':
  Root=BinaryTree(20)
  Root.addNode(23)
  Root.addNode(21)
  Root.addNode(24)
  Root.addNode(19)
  Root.listToTree([2,4,5,6,23,12,56,43,32,12,78])
  Root.printTree()


    