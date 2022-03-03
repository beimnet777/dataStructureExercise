"""The graph takes all edges(list of tuples) in the graph at
 the begging and uses adjecency list to represtet
 the grapth"""
from importlib.resources import path
from queue import Queue


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
  def breadth_first_traversal(self,start):
    queue=Queue()
    visited={}
    queue.put(start)

    while queue.not_empty:
      visit=queue.get()
      visited[visit]=True
      if visit in self.dict.keys():
        for i in self.dict[visit]:
          if i is not visited:
            queue.put(i)
  def shortest_path_bft(self,start,end):
    queue=Queue()
    queue.put(start)
    visited={}
    prev={}
    flag=0
    while queue.not_empty:
      visit=queue.get()
      visited[visit]=True
      if visit in self.dict.keys():
        for i in self.dict[visit]:
          if i not in visited:
            prev[i]=visit
            if i==end:
              flag=1
              break
            queue.put(i)  
        if flag==1:
          break
    path=[]
    keys=list(prev.keys())
    values=list(prev.values())    
    if end in prev.keys() :
      
      while start!=end:
        path.append(start)
        start=keys[values.index(start)]
      # path.reverse()
    print(start)
    return path, prev

      


      

  
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
  print(Graph.search_path('A','M'))
  print(Graph.shortest_path('A','M'))
  print(Graph.shortest_path_bft('A','M'))
