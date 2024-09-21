from collections import deque

vertex_count, edge_count, start_node = map(int, input().split())
visit = [False] * (vertex_count + 1)

graph = [[0]*(vertex_count+1) for _ in range(vertex_count+1)]
for i in range (edge_count):
    a,b = map(int,input().split())
    graph[a][b] = graph[b][a] = 1
    
def dfs(s_node):
    visit[s_node] = True
    print(s_node, end = ' ')
    for i in range(1, vertex_count + 1):
        if graph[s_node][i] == 1 and not visit[i]:
            dfs(i)

def bfs(s_node):
    q = deque([s_node])
    visit[s_node] = True
    
    while len(q) > 0:
        s = q.popleft()
        print(s, end = ' ')
        for i in range(1, vertex_count + 1):
            if graph[s][i] == 1 and not visit[i]:
                visit[i] = True
                q.append(i)
        
dfs(start_node)
visit = [False] * (vertex_count + 1)
print()
bfs(start_node)