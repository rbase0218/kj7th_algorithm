def is_prime_number(x):
    for j in range(2, x + 1):
        if x % j == 0:
            if x == j:
                return True
            break
    return False    

n = int(input())

for _ in range(n):
    count = int(input())
    
    a = count // 2
    b = count // 2
    
    while True:
        if is_prime_number(a) and is_prime_number(b):
            print(f'{a} {b}')
            break
        else:
            a -= 1
            b += 1