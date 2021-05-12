# Dongyoung Kwon @Chuncheonian (ehddud2468@gmail.com)
parent = dict()
rank = dict()
check = 0
hi = 0

def make_singleton_set(v):
    parent[v] = v
    rank[v] = 1

def find(v):
    global check
    check += 1
    print('find', check)
    if parent[v] != v:
        parent[v] = find(parent[v])
    return parent[v]

def union(r1, r2):
    global hi
    hi += 1
    print('union', hi)
    if r1 != r2:
        if rank[r1] > rank[r2]:
            parent[r2] = r1
            rank[r1] += rank[r2]
        else:
            parent[r1] = r2
            if rank[r1] == rank[r2]:
                rank[r2] += rank[r1]

def kruskal(graph):
    for v in graph['vertices']:
        make_singleton_set(v)
    mst = set()
    edges = list(graph['edges'])
    edges.sort()
    for edge in edges:
        weight, v1, v2 = edge
        print(mst)
        r1 = find(v1)
        r2 = find(v2)
        print(mst)
        print()
        if r1 != r2:
            union(r1, r2)
            mst.add(edge)
    return mst

graph = { 
    'vertices': ['A', 'B', 'C', 'D', 'E'],
    'edges': set([(1, 'A', 'B'),
                  (2, 'A', 'C'),
                  (3, 'B', 'C'),
                  (7, 'B', 'D'),
                  (6, 'C', 'D'),
                  (5, 'C', 'E'),
                  (4, 'D', 'E')])
    }

mst = kruskal(graph)
print("F : ", mst)
print(check)