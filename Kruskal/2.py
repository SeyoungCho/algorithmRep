#2022-08-15
#1
#no. of nodes
v = 7
#no. of edges
e = 9
#graph (cost, a, b)
edges = [(29, 1, 2), (35, 2, 3), (7, 3, 4), (75, 1, 5), (53, 5, 6), (23, 4, 6),
         (13, 4, 7), (25, 6, 7), (34, 2, 6)]

result = []
min_cost = 0

def find_parent(parent, x):
	if x != parent[x]:
		return find_parent(parent, parent[x])
	else:
		return parent[x]

def union_parent(parent, a, b):
	a = find_parent(parent, a)
	b = find_parent(parent, b)
	if a < b:
		parent[b] = a
	else:
		parent[a] = b

#initialize parent table
parent = [0] * (v + 1)
for i in range(1, v + 1):
	parent[i] = i

#sort the edges in ascending order of wedges
edges.sort()
for edge in edges:
	cost, a, b = edge
	# if there is not a cycle
	if find_parent(parent, a) != find_parent(parent, b):
		union_parent(parent, a, b)
		result.append((cost, a, b))
		min_cost += cost

print("tree: ", result)
print("minimum cost: ", min_cost)
