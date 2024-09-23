import sys
sys.setrecursionlimit(10**6)

def dfs(start_node):
    for i in graph[start_node]:
        if visit[i] == False:
            visit[i] = True
            parents[i] = start_node
            dfs(i)
    
if __name__ == '__main__':
    n_count = int(sys.stdin.readline())

    # 인접 행렬 생성
    graph = [[] for i in range(n_count + 1)]
    for i in range(n_count - 1):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    # 방문 여부 및 Parent Node    
    visit = [False] * (n_count + 1)
    parents = [0] * (n_count + 1)

    dfs(1)
    
    for i in range(2, len(parents)):
        print(parents[i])