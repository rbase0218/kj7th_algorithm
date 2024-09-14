def power(a : int, b : int, c : int):
    if b == 1 :
        return a % c

    temp = power(a, b // 2, c)
    if b % 2 == 1:
        return ((temp * temp) % c) * a % c
    else:
        return (temp * temp) % c

a, b, c = map(int, input().split())
sum = power(a,b,c)
print(sum)