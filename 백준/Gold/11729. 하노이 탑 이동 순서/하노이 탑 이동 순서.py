def hanoi(count : int, start, end):
    if count == 1:
        print(start, end)
        return
    
    hanoi(count - 1, start, 6 - (start + end))
    print(start, end)
    hanoi(count - 1, 6 - (start +end), end)

n = int(input())
print(2**n-1)
hanoi(n, 1, 3)