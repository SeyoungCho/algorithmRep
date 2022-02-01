#2022-02-01
#1
#DFS uses stack data structure
# 1. push the start node into stack
# 2. if the top node in the stack has one or more unvisited 
#    adjacent nodes, push them into the stack and visit them. 
#    if the top node doesn't have any unvisited adjacent node, 
#    pop the node from the stack
# 3. repeat step 2 until no more nodes have unvisited adjacent nodes

def dfs(graph, v, visited):
  #visit the current node
  visited[v] = True
  print(v, end=' ')
  #recursively visit the nodes that are adjacent to the current node 
  for i in graph[v]:
    if not visited[i]:
      dfs(graph, i, visited)

graph = [
  [], 
  [2,3,8],
  [1,7],
  [1,4,5],
  [3,5],
  [3,4],
  [7],
  [2,6,8],
  [1,7]
]

visited = [False] * 9

dfs(graph, 1, visited)
print()