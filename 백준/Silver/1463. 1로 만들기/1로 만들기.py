import sys

def dp(target_num):
    dp_table = [0] * (target_num + 1)
    
    for i in range(2, target_num + 1):
        dp_table[i] = dp_table[i - 1] + 1
        
        if i % 2 == 0:
            dp_table[i] = min(dp_table[i], dp_table[i // 2] + 1)
        if i % 3 == 0:
            dp_table[i] = min(dp_table[i], dp_table[i // 3] + 1)
        
    return dp_table[target_num]

if __name__ == "__main__":
    num = int(input())
    print(dp(num))