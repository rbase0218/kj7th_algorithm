import sys
from collections import deque
sys.setrecursionlimit(10**6)

def bfs() -> int:
    q = deque()
    indoor = 0
    sum = 0
    visit = [False] * (n_count + 1)
    
    # 전체 순회
    for i in range(1, n_count + 1):
        # 방문 여부 초기화 -> 새로운 노드가 돈다면
        # 실내일 경우 제외한다.
        if n_type[i - 1] == '1' or visit[i]:
            continue
        
        q.append(i)
        
        while q:
            cur_node = q.popleft()
            if n_type[cur_node - 1] == '0':
                visit[cur_node] = True
                
            # 인접 노드 확인
            for adj in graph[cur_node]:
                if visit[adj]:
                    continue
                
                if n_type[adj - 1] == '1':
                    sum += 1
                elif n_type[adj - 1] == '0':
                    q.append(adj)

        if sum <= 1:
            sum = 0
        indoor += sum * (sum - 1)
        sum = 0
    return indoor
                
if __name__ == '__main__':
    answer = 0
    n_count = int(input())
    n_type = input()

    graph = [ [] for _ in range(n_count+1)]

    for _ in range(n_count - 1):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
        
        if n_type[a - 1] == n_type[b - 1] == '1':
            answer += 2
    print(bfs() + answer)