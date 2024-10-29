def dp():
    if num < 3:
        return 1
    
    table = [1] * (num + 1)
    table[1] = 1
    table[2] = 1
    
    for i in range(3, num + 1):
        table[i] = table[i - 1] + table[i - 2]
    
    return table[num]

if __name__ == "__main__":
    num = int(input())
    print(dp())