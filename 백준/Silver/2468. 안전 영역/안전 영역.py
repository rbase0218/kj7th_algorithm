import sys
sys.setrecursionlimit(100000)
# 상 -> 하 -> 좌 -> 우
dx = [ -1, 1, 0, 0 ]
dy = [ 0, 0, -1, 1 ]

region_count = int(input())
# 각 지역에 따른 안전 강수량을 입력 받는다.
region_height_matrix = [list(map(int, input().split())) for _ in range(region_count)]

safe_region_count = 0

def dfs(x, y, h):
    # 이동 위치에 대한 정보
    for i in range(4):
        # 만약 이동하려는 위치가 방문하지 않았다면 False
        nx = x + dx[i]
        ny = y + dy[i]
        
        # 다음 범위가 0을 초과하거나 len을 넘길 경우
        # 혹은 이미 방문한 장소일 경우
        # 혹은 강수량보다 작을 경우
        if (nx < 0 or nx >= region_count or ny < 0 or ny >= region_count or
            region_visit[nx][ny] == True or region_height_matrix[nx][ny] < h):
            continue
        
        region_visit[nx][ny] = True
        dfs(nx, ny, h)

# 각 지역 중에서 가장 강수량이 높은 것
for k in range(0, 101):
    # 강수량이 새로워질수록 새로운 Visit 배열을 만들어준다.
    region_visit = [[False for i in range(region_count)] for j in range(region_count)]
    count = 0
    
    for i in range(region_count):
        for j in range(region_count):
            if region_visit[i][j] == True or region_height_matrix[i][j] < k:
                continue
            else:
                region_visit[i][j] = True
                count += 1
                dfs(i, j, k)
    safe_region_count = max(safe_region_count, count)

print(safe_region_count)