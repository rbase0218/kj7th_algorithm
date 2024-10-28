import sys

def dp():
    table = [0] * (days + 1)
    
    for i in range(days):
        for j in range(i + schedule[i][0], days+1):
            if table[j] < table[i] + schedule[i][1]:
                table[j] = table[i] + schedule[i][1]
    return table[-1]

if __name__ == "__main__":
    days = int(input())
    
    # [i][0] == Day
    # [i][1] == Money
    schedule = [list(map(int, input().split())) for _ in range(days)]
    
    print(dp())