from math import gcd

def divisors(n):
    table = set()
    
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            table.add(i)
            table.add(n // i)
    
    return sorted(list(table))

if __name__ == "__main__":
    a, b = map(int, input().split())
    
    # a와 b의 최대 공약수를 구한다.
    max_num = gcd(a, b)
    # 최대 공약수의 약수를 구한다.
    numbers = divisors(max_num)
    # 최대 공약수의 약수를 오름차순 정렬하고 순회한다.
    
    for i in numbers:
        print(i, int(a/i), int(b/i))
    
    