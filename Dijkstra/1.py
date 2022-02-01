#2022-02-01
#1
import heapq
INF = int(1e9)
#no. of nodes : 6
#no. of edges : 11
#start node number : 1
graph = [
  [],
  [(2,2), (3,5), (4,1)],
  [(3,3), (4,2)],
  [(2,3), (6,5)],
  [(3,3), (5,1)],
  [(3,1), (6,2)],
  []
]
distance = [INF] * 7

def dijkstra(start):
  q = []
  # 0 cost for the start node, push the start node into the priority queue
  heapq.heappush(q, (0, start))
  distance[start] = 0
  while q: # if the queue is not empty
    #get the info about the node with the shortest distance 
    dist, now = heapq.heappop(q)
    #if the current node has already been confirmed, continue
    if distance[now] < dist:
      continue
    #check the adjacent nodes from the current node
    for i in graph[now]:
      cost = dist + i[1]
      #update if the cost evaluated is smaller than the one in the distance table
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))

dijkstra(1)

for i in range(1, 7):
  #if unreacheable, print 'infinity'
  if distance[i] == INF:
    print("shortest path from 1 to %d : INFINITY" %i)
  else:
    print("shortest path from 1 to %d : %d" %(i, distance[i]))

