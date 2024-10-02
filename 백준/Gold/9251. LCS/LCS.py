import sys

def lcs(str1, str2):
    str1_len = len(str1)
    str2_len = len(str2)
    
    dp_table = [[0] * (str2_len + 1) for _ in range(str1_len + 1)]
    
    for i in range(1, str1_len + 1):
        for j in range(1, str2_len + 1):
            if str1[i - 1] == str2[j - 1]:
                dp_table[i][j] = dp_table[i - 1][j - 1] + 1
            else:
                dp_table[i][j] = max(dp_table[i - 1][j], dp_table[i][j - 1])
    return dp_table[str1_len][str2_len]

if __name__ == "__main__":
    str1 = input()
    str2 = input()
    print(lcs(str1, str2))