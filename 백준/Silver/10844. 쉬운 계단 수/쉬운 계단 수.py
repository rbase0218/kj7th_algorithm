import sys

def dp():
    dp_table = [[0] * 10 for _ in range(num + 1)]
    
    for i in range(1, 10):
        dp_table[1][i] = 1
    
    for i in range(2, num + 1):
        for j in range(0, 10):
            if j == 0:
                dp_table[i][j] = dp_table[i - 1][j + 1] 
            elif j >= 1 and j <= 8:
                dp_table[i][j] = dp_table[i - 1][j - 1] + dp_table[i - 1][j + 1]
            elif j == 9:
                dp_table[i][j] = dp_table[i - 1][j - 1]
                
    sum = 0    
    for n in dp_table[num]:
        sum = sum + n
    return sum % 1000000000;

if __name__ == "__main__":
    num = int(input())
    print(dp())
    