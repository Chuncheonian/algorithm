# Dongyoung Kwon @Chuncheonian (ehddud2468@gmail.com)
# python version requirement: >=3.9

from collections import deque

# breadth-first-seacrch algorithm
def bfs(graph: dict, start_vertex: any) -> list[any]:
    visited = [start_vertex]        # visited : 방문한 vertex를 담고있는 리스트
    queue = deque([start_vertex])   # dfs는 queue를 이용
    
    while queue:  # queue에 남은 것이 없을 때까지 반복
        vertex = queue.popleft()  # vertex : 현재 방문하고 있는 vertex
        
        # 현재 vertex의 자식 vertex들 탐색
        for w in graph[vertex]:
            # 현재 vertex를 방문한 적 없는 경우
            if w not in visited:
                visited.append(w)
                queue.append(w)
    return visited

# Testcase
adjacency_graph = { 1: [2, 3, 4],
                    2: [5],
                    3: [5],
                    4: [],
                    5: [6, 7],
                    6: [],
                    7: [3]}

print(bfs(adjacency_graph, 1))  # > 1, 2, 3, 4, 5, 6, 7