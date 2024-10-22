import sys

def dp():
    for i in range(1, count):
        for j in range(i):
            if numbers[i] > numbers[j]:
                table[i] = max(table[i], table[j] + 1)
    return max(table)    

if __name__ == "__main__":
    count = int(input())
    numbers = list(map(int, input().split()))
    table = [1] * (count + 1);
    
    print(dp())