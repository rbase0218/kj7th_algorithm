if __name__ == "__main__":
    # Input
    n, x = map(int, input().split())
    table = list(map(int, input().split()))
    
    value = sum(table[:x])
    max_value = value
    count = 1
    
    for i in range(x, n):
        value -= table[i - x]
        value += table[i]
        
        if value > max_value:
            max_value = value
            count = 1
        elif value == max_value:
            count += 1
    
    if max(table) == 0:
        print('SAD')
    else:        
        print(max_value)
        print(count)