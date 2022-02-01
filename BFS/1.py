#2022-02-01
#1
#BFS uses queue data structure
# 1. push the start node into the queue
# 2. pop from the queue and push all the unvisited adjacent node
#    and visit them
# 3. repeat step 2 until no more nodes have unvisited adjacent nodes
from collections import deque

def bfs(graph, start, visited):
  #use deque library to implement queue
  queue = deque([start])
  #visit current node
  visited[start] = True
  #repeat until the queue is empty
  while queue:
    #pop from the queue and print it
    v = queue.popleft()
    print(v, end=' ')
    #push all the unvisited adjacent nodes
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True

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

bfs(graph, 1, visited)
print()