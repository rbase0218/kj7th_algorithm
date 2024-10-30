import sys
sys.setrecursionlimit(10 ** 8)

def dfs(x, y):
    # 도착 했을 경우 증가
    if x == width - 1 and y == height - 1:
        return 1
    # -1이 아닐 경우, 그대로 전달.
    if table[y][x] != -1:
        return table[y][x]
    
    count = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < width and 0 <= ny < height and numbers[y][x] > numbers[ny][nx]:
            count += dfs(nx, ny)
            
    table[y][x] = count
    return table[y][x]

if __name__ == "__main__":
    height, width = map(int, input().split())
    numbers = [list(map(int, input().split())) for _ in range(height)]
    table = [ [-1] * width for _ in range(height)]
    # 상하좌우
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    print(dfs(0, 0))