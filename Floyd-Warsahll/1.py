#2022-02-01
#1
INF = int(1e9)
#no. of nodes : 4
#no. of edges : 7
#start node number : 1

graph = [[INF] * (5) for i in range(5)]

graph[1][2] = 4
graph[1][4] = 6
graph[2][1] = 3
graph[2][3] = 7
graph[3][1] = 5
graph[3][4] = 4
graph[4][3] = 2

for a in range(1, 5):
  for b in range(1,5):
    if a == b:
      graph[a][b] = 0


def floyd_warshall(graph, n): #n is the number of nodes
  for i in range(1, n+1):
    for j in range(1, n+1):
      if j == i:
        continue
      for k in range(1, n+1):
        graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])

floyd_warshall(graph, 4)

for i in range(1, 5):
  for j in range(1, 5):
    if graph[i][j] == INF:
      print("INF", end =" ")
    else:
      print(graph[i][j], end=" ")
  print()