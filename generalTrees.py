class TreeNode:
  def __init__(self,data):
    self.data=data
    self.children=[]
    self.parent=None
  def addChild(self,child:TreeNode):
    child.parent=self
    self.children.append(child)
