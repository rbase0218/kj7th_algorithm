import sys

def dp(st):
    if len(st) <= 2:
        return sum(st)
    else:
        dp_table[1] = stairs[1]
        dp_table[2] = stairs[1] + stairs[2]

        for i in range(3, len(st)):
            dp_table[i] = max(dp_table[i - 2] + stairs[i], dp_table[i - 3] + stairs[i - 1] + stairs[i])

    return dp_table[len(st) -1]

if __name__ == '__main__':
    stairs_count = int(input())
    stairs = [0]
    stairs += [int(input()) for _ in range(stairs_count)]
    dp_table = [ 0 for _ in range(stairs_count + 1)]
    
    print(dp(stairs))