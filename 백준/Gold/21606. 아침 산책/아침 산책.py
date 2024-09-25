import sys
from collections import deque
sys.setrecursionlimit(10**6)

def bfs() -> int:
    q = deque()
    answer = 0
    
    for i in range(1, n_count + 1):
        visit = [False] * (n_count + 1)
        
        if n_type[i - 1] == '0':
            continue

        visit[i] = True
        q.append(i)
        
        while q:
            curr_node = q.popleft()
            visit[curr_node] = True
            for adj_node in graph[curr_node]:
                if visit[adj_node] == False:
                    if n_type[adj_node - 1] == '1':
                        answer += 1
                    else:
                        q.append(adj_node)
    return answer

if __name__ == '__main__':
    n_count = int(input())
    n_type = input()

    graph = [[] for _ in range(n_count+1)]

    for _ in range(n_count - 1):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
    
    print(bfs())