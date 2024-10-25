import sys

def dp():
    table = [0] * (count)
    
    for i in range(0, count):
        if table[i - 1] + num_list[i] > num_list[i]:
            table[i] = table[i - 1] + num_list[i]
        else:
            table[i] = num_list[i]
    
    return max(table)

if __name__ == "__main__":
    count = int(input())
    num_list = list(map(int, input().split()))
    
    print(dp())