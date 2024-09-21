import sys
sys.setrecursionlimit(10**6)

n_count, e_count = map(int, sys.stdin.readline().split())

# 인접 행렬 생성
graph = [[0]*(n_count+1) for _ in range(n_count+1)]
for i in range (e_count):
    a,b = map(int, sys.stdin.readline().split())
    graph[a][b] = graph[b][a] = 1
# 방문 여부 확인
visit = [False] * (n_count + 1)
sum = 0

def dfs() -> int:
    global sum
    for i in range(1, len(graph)):
        for j in range(1, len(graph[i])):
            if visit[j] == False:
                dfs_visit(j)
                sum += 1
    return sum
                
def dfs_visit(node):
    visit[node] = True
    
    for i in range(len(graph[node])):
        if graph[node][i] == 1 and visit[i] == False:
            dfs_visit(i)
            
if __name__ == '__main__':
    print(dfs())