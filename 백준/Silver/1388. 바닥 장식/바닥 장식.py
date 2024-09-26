import sys

def dfs():
    # -면, 같은 행만 검색해도 충분하다.
    # |면, 같은 열만 검색해도 충분하다.
    # 각자 탐색 종료 조건은 같은 행/렬에서 자신과 다른 문자가 나온다면.
    # 그리고 탐색이 종료되었고 더이상 탐색할 필요가 없는 친구에 한해서만 Visit[True]
    # 해둔다면? 시간을 조금 더 단축시킬 수 있지.
    # 사실 그래프 탐색 보다는 행렬 탐색이긴 해!
    
    for i in range(room_height):
        for j in range(room_width):
            if not visit[i][j]:
                dfs_visit(planks[i][j], j, i)
            
def dfs_visit(node, x, y):
    global planks_count
    
    if node == '-': # Node가 -이면, 같은 Width만 탐색한다.
        for i in range(x, room_width):
            if visit[y][i] and planks[y][i] != node:
                planks_count += 1
                break
            
            if planks[y][i] == node:
               visit[y][i] = True
               
               if i >= room_width - 1:
                   planks_count += 1
                   
            elif planks[y][i] != node:
                planks_count += 1
                break
            
    elif node == '|': # Node가 |이면, 같은 Height만 탐색한다.
        for i in range(y, room_height):
            if visit[i][x] and planks[y][i] != node:
                planks_count += 1
                break
            
            if planks[i][x] == node:
                visit[i][x] = True
                
                if i >= room_height - 1:
                    planks_count += 1
                
            elif planks[i][x] != node:
                planks_count += 1
                break

if __name__ == '__main__':
    room_height, room_width = map(int, input().split())
    planks = [input() for __ in range(room_height)]
    visit = [[False] * (room_width) for _ in range(room_height)]
    planks_count = 0
    
    dfs()
    print(planks_count)