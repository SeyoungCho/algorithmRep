#2023-02-09
#181
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
	distance[start] = 0
	q = []
	heapq.heappush(q, (distance[start], start))
	while q:
		dist, now = heapq.heappop(q)
		if distance[now] < dist:
			continue
		for i in graph[now]:
			cost = i[1] + dist
			if cost < distance[i[0]]:
				distance[i[0]] = cost
				heapq.heappush(q, (cost, i[0]))

dijkstra(1)
for i in range(1, len(distance)):
	if distance[i] == INF:
		print("Shortest distance from 1 to %d is INF"%i)
	else:
		print("Shortest distance from 1 to %d is %d"%(i, distance[i]))