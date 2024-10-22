import sys

if __name__ == "__main__":
    count = int(input())
    numbers = [int(input()) for _ in range(count)]
    
    table = [0] * (max(numbers) + 1);
    table[1] = 1
    table[2] = 2
    table[3] = 4
    table[4] = 7
    table[5] = 13
    table[6] = 24
    table[7] = 44
    table[8] = 81
    table[9] = 149
    table[10] = 274
    
    for i in numbers:
        print(table[i])
