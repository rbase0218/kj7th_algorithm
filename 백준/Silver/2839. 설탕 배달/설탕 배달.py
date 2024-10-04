import sys

def dp(kg):
    if kg == 3 or kg == 5:
        return 1
    if kg < 6:
        return -1

    dp_table = [-1] * (kg + 1);
    dp_table[3] = 1
    dp_table[5] = 1    
    
    for i in range(6, kg + 1):
        if dp_table[i - 3] != -1:
            dp_table[i] = dp_table[i - 3] + 1
        
        if dp_table[i - 5] != -1:
            if dp_table[i] == -1 or dp_table[i - 5] + 1 < dp_table[i]:
                dp_table[i] = dp_table[i - 5] + 1
                
    return dp_table[kg]
               

if __name__ == "__main__":
    kg = int(input())
    print(dp(kg))