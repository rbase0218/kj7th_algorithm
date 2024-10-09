import sys
from collections import deque

def topological_sort():
    queue = deque()
    
    for i in range(1, std_num + 1):
        if indegree[i] == 0:
            indegree[i] = -1
            queue.append(i)
    while queue:
        num = queue.popleft()
        print(num, end=" ")
        for i in graph[num]:
            indegree[i] -= 1
            
            if indegree[i] == 0:
                queue.append(i)

if __name__ == "__main__":
    std_num, change_num = map(int, input().split())
    
    # 진입차수
    indegree = [0] * (std_num + 1)
    
    # Graph
    graph = [[] for _ in range(std_num + 1)]
    for _ in range(change_num):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1
    
    topological_sort()