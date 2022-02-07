#2022-02-07
#7
import heapq
INF = int(1e9)
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
  distance[start] = 0
  heapq.heappush(q, (0,start))
  while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
      continue
    for i in graph[now]:
      cost = dist + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))

dijkstra(1)
for i in range(1, len(distance)):
  if distance[i] == INF:
    print("Shortest path from 1 to %d is INF" %(i))
  else:
    print("Shortest path from 1 to %d is %d" %(i, distance[i]))
  
      