"""The graph takes all edges(list of tuples) in the graph at
 the begging and uses adjecency list to represtet
 the grapth"""
class GraphNode:
  def __init__(self,edges):
    self.edges=edges
    self.dict={}
    for i,j in edges:
      if i in self.dict.keys():
        self.dict[i].append(j)
      else:
        self.dict[i]=[j]
    print (self.dict)
  
if __name__=='__main__':
  edges=[('A','B'),
  ('A','C'),
  ('B','F'),
  ('A','F'),
  ('F','D'),
  ('D','M'),
  ('M','B'),
  ('B','E'),
  ('E','G')]
  Graph=GraphNode(edges)
