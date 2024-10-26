import sys

def dp(num):
    if num < 3:
        return 1
    
    table = [1] * (num + 1)
    
    for i in range(4, num + 1):
        table[i] = table[i - 2] + table[i - 3]
        
    return table[num]
    
if __name__ == "__main__":
    count = int(input())
    
    for _ in range(count):
        num = int(input())
        print(dp(num))