from collections import deque

computer_count = int(input())
connect_count = int(input())

graph = [[0]*(computer_count+1) for _ in range(computer_count+1)]
for i in range (connect_count):
    a,b = map(int,input().split())
    graph[a][b] = graph[b][a] = 1
visit = [False] * (computer_count + 1)

sum = 0
def bfs(node) -> int:
    global sum
    q = deque([node])
    visit[node] = True
    
    while len(q) > 0:
        s = q.popleft()
        for i in range(1, computer_count + 1):
            if graph[s][i] == 1 and not visit[i]:
                visit[i] = True
                sum = sum + 1
                q.append(i)
                
        visit[s] = True
    return sum

print(bfs(1))