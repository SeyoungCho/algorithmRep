#2023-03-11
#96
#no. of nodes
v = 7
#no. of edges
e = 9
#graph (cost, a, b)
edges = [(29, 1, 2), (35, 2, 3), (7, 3, 4), (75, 1, 5), (53, 5, 6), (23, 4, 6),
         (13, 4, 7), (25, 6, 7), (34, 2, 6)]

result = []
parent = [0] * (v + 1)
min_cost = 0

for i in range(1, v+1):
	parent[i] = i

def find_parent(parent, x):
	if parent[x] == x:
		return parent[x]
	else:
		return find_parent(parent, parent[x])

def union_parent(parent, a, b):
	a = find_parent(parent, a)
	b = find_parent(parent, b)
	if a < b:
		parent[b] = a
	else:
		parent[a] = b

edges.sort()
for edge in edges:
	cost, a, b = edge
	if find_parent(parent, a) != find_parent(parent, b):
		result.append(edge)
		union_parent(parent, a, b)
		min_cost += cost

print("result: ", result)
print("minimum cost: ", min_cost)