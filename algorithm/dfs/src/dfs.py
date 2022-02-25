# Dongyoung Kwon @Chuncheonian (ehddud2468@gmail.com)
# python version requirement: >=3.9

# 재귀 dfs는 사전적 순서로 방문
def dfs_recursive(graph: dict, vertex: any, visited=[]) -> list[any]:
    visited.append(vertex)
    
    for node in graph[vertex]:
        if node not in visited:
            dfs_recursive(graph, node, visited)
    
    return visited

# 반복 dfs는 stack을 사용하기 때문에 역순으로 방문
def dfs_iteration(graph: dict, start_vertex: any) -> list[any]:
    visited = []            # visited : 방문한 vertex를 담고있는 리스트
    stack = [start_vertex]  # dfs의 반복 구현은 stack을 이용
    
    while stack:  # 스택에 남은것이 없을 때까지 반복
        vertex = stack.pop()  # vertex : 현재 방문하고 있는 vertex
        
        # 현재 vertex를 방문한 적 없는 경우
        if vertex not in visited:
            visited.append(vertex)
            for w in graph[vertex]:  # 현재 vertex의 자식 vertex들을 stack에 추가
                stack.append(w)
    
    return visited

# Testcase
adjacency_graph = { 1: [2, 3, 4],
                    2: [5],
                    3: [5],
                    4: [],
                    5: [6, 7],
                    6: [],
                    7: [3] }

print(dfs_recursive(adjacency_graph, 1))  # > 1, 2, 5, 6, 7, 3, 4
print(dfs_iteration(adjacency_graph, 1))  # > 1, 4, 3, 5, 7, 6, 2