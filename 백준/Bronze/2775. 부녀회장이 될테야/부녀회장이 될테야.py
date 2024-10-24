import sys

def dp(floor, room):
    dp_table = [[0] * (room + 1) for _ in range(floor + 1)]
    
    for i in range(1, room + 1):
        dp_table[0][i] = i
        
    for i in range(1, floor + 1):
        for j in range(1, room + 1):
            dp_table[i][j] = dp_table[i - 1][j] + dp_table[i][j - 1]
        
    return dp_table[floor][room]

if __name__ == "__main__":
    count = int(input())
    
    for _ in range(count):
        floor = int(input())
        room = int(input())
        print(dp(floor, room))