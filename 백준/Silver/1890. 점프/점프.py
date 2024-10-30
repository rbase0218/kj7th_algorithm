# import sys
# sys.setrecursionlimit(10 ** 8)
# sys.stdin = open('input.txt', 'r')

# def dp(x, y):
#     # 목적지에 도착했을 경우 1을 반환한다.
#     if x == count - 1 and y == count - 1:
#         return 1
    
#     if table[y][x] != 0:
#         return table[y][x]
    
#     num = 0
#     for i in range(2):
#         nx = x + (dx[i] * graph[y][x])
#         ny = y + (dy[i] * graph[y][x])
#         if 0 <= nx < count and 0 <= ny < count:
#             num += dp(nx, ny)

#     table[y][x] = num
#     return table[y][x]

# if __name__ == "__main__":
#     count = int(sys.stdin.readline())
#     graph = [list(map(int, sys.stdin.readline().split())) for _ in range(count)]
#     table = [ [0] * count for _ in range(count)]
    
#     # 우 -> 하
#     dx = [1, 0]
#     dy = [0, 1]
    
#     print(dp(0, 0))

n = int(input())
d = [None]*n

for i in range(n):
    d[i] = list(map(int,input().split())) #입력

dp = [[0] * n for _ in range(n)] #dp
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if d[i][j] == 0:continue #(0,0)이면 이동할 수 없으므로 값을 더해줄 필요가 없음
        if j + d[i][j] < n:
            dp[i][j+d[i][j]] += dp[i][j] #(i,j)에서 오른쪽으로 이동할 수 있는 칸
        if i + d[i][j] < n:
            dp[i+d[i][j]][j] += dp[i][j] #(i,j)에서 아래로 이동할 수 있는 칸

print(dp[n-1][n-1])