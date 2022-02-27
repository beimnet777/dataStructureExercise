class TreeNode:
  def __init__ (self,data:list):
    self.data=data 
    self.parent=None
    self.children=[]
  def addChild(self,TreeNode):
    self.children.append(TreeNode)
    TreeNode.parent=self
  def getLevel(self):
    counter=0
    while self.parent:
      counter+=1
      self=self.parent
    return counter

  def printTree(self,dataType:int): #1 for key 2 for value 3 for both:
    decoration="   " * self.getLevel() +"--|" if self.getLevel()!=0 else " "
    if dataType==0:
      print(decoration+self.data[0])
    if dataType==1:
      print(decoration+self.data[1])
    if dataType==2:
      print(decoration+self.data[0]+'('+self.data[1]+')')
    if self.children:
      for i in self.children:
        i.printTree(dataType)
if __name__=='__main__':
  Root=TreeNode(['Root','CEO'])

  branch1=TreeNode(['banch1','CTO'])

  leaf11=TreeNode(['leaf11','HEAD'])
  leaf12=TreeNode(['leaf12','HEAD'])

  branch1.addChild(leaf11)
  branch1.addChild(leaf12)

  

  branch2=TreeNode(['branch2','CTO'])

  leaf21=TreeNode(['leaf21','HEAD'])
  leaf22=TreeNode(['leaf22','HEAD'])

  branch2.addChild(leaf21)
  branch2.addChild(leaf22)

  Root.addChild(branch1)
  Root.addChild(branch2)
  Root.printTree(2)

