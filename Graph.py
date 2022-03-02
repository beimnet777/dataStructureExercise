"""The graph takes all edges(list of tuples) in the graph at
 the begging and uses adjecency list to represtet
 the grapth"""
from importlib.resources import path


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
  def search_path(self,start,end,path=[]):
    path=path+[start]
    if start==end:
      return [path]
    if start not in self.dict.keys():
      return []
    all_paths=[]
    for i in self.dict[start]:
      if i not in path:
        paths=self.search_path(i,end,path)
      for i in paths:
        all_paths.append(i)
    return all_paths
      

  
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
  print(Graph.search_path('A','F'))
