#2022-02-06
#6
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
  distance[start] = 0
  q = []
  heapq.heappush(q, (distance[start], start))
  while q:
    dist, now = heapq.heappop(q)
    for i in graph[now]:
      if distance[now] < dist:
        continue
      cost = dist + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q,(cost, i[0]))

dijkstra(1)
for i in range(1, 7):
  if distance[i] == INF:
    print("Shortest path from 1 to %d : INF" %i)
  else:
    print("Shortest path from 1 to %d : %d"%(i, distance[i]))
       