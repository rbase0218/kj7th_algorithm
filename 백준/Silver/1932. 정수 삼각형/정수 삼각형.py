import sys

def dp():
    table = [[0] * (i + 1) for i in range(count)]
    
    for i in range(count):
        for j in range(len(numbers[i])):
            if j == 0:
                table[i][j] = numbers[i][j] + table[i-1][0]
            elif j == len(numbers[i]) - 1:
                table[i][j] = numbers[i][j] + table[i-1][j - 1]
            else:
                table[i][j] = max(numbers[i][j] + table[i-1][j-1],
                                numbers[i][j] + table[i-1][j])
    
    return max(table[count - 1])

if __name__ == "__main__":
    count = int(input())
    numbers = []
    for _ in range(count):
        numbers.append(list(map(int, input().split())))
        
    print(dp())