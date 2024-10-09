import sys

def dp():
    dp_table = [0] * (num + 1)
    
    dp_table[0] = 0
    dp_table[1] = 1
    
    for i in range(2, num + 1):
        dp_table[i] = dp_table[i - 1] + dp_table[i - 2]
    
    return dp_table[num]
    
if __name__ == "__main__":
    num = int(input())
    print(dp())