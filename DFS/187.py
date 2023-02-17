#2023-02-17
#187
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

def dfs(graph, v, vistied):
	print(v, end=' ')
	visited[v] = True
	for i in graph[v]:
		if not visited[i]:
			dfs(graph, i, visited)

dfs(graph, 1, visited)
print()