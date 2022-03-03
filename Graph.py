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
  def shortest_path(self,start,end):
    paths=self.search_path(start,end)
    print(paths)
    short=len(paths[0])
    index=0
    for i in range(len(paths)):
      if len(paths[i])<short:
        short=len(paths[i])
        index=i

    return paths[index]
  def short_path(self,start,end,path=[]):
    pass
      

  
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
  print(Graph.search_path('A','E'))
  print(Graph.shortest_path('A','M'))
