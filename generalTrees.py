class TreeNode:
  def __init__(self,data):
    self.data=data
    self.children=[]
    self.parent=None
  def addChild(self,child):
    child.parent=self
    self.children.append(child)
  def getLevel(self):
    counter=0
    while self.parent:
      counter+=1
      self=self.parent
    return counter
  def printLevel(self,level:int):
    pass

  def printTree(self,level:int):
    """
    recursively printing the data of children and for each children the level decreases as we
    dropped one level when the childrentree node is accessed
        """
    decoration='  ' * self.getLevel()+ '--|' if self.parent!=None else ''
    print(decoration+self.data)
    if self.getLevel()<level:
      if len(self.children)!=0:
        for i in self.children:
          i.printTree(level-1)

if __name__=='__main__':
  Root=TreeNode('Root')

  branch1=TreeNode('banch1')

  leaf11=TreeNode('leaf11')
  leaf12=TreeNode('leaf12')

  branch1.addChild(leaf11)
  branch1.addChild(leaf12)

  

  branch2=TreeNode('branch2')

  leaf21=TreeNode('leaf21')
  leaf22=TreeNode('leaf22')

  branch2.addChild(leaf21)
  branch2.addChild(leaf22)

  Root.addChild(branch1)
  Root.addChild(branch2)
  Root.printTree(4)
  
