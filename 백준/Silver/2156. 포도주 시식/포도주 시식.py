import sys

def dp():
    if count == 1:
        return numbers[0]
    elif count == 2:
        return numbers[0] + numbers[1]
    
    table = [0] * (count + 1)
    table[0] = numbers[0]
    table[1] = numbers[1] + numbers[0]
    
    for i in range(2, count):
        table[i] = max(table[i - 1], 
                    numbers[i] + numbers[i - 1] + table[i - 3],
                    numbers[i] + table[i - 2])
    
    return max(table)

if __name__ == "__main__":
    count = int(input())
    numbers = [int(input()) for _ in range(count)]
    
    print(dp())