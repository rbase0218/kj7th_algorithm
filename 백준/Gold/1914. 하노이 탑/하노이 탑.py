def move(no, x, y):
    if no == 1 :
        print(x,y)
        return
    
    move(no - 1, x, 6 - x - y)
    print(x,y)
    move(no - 1, 6 - x - y, y)
    
n = int(input())
print(2**n-1)

if n <= 20:
    move(n, 1, 3)