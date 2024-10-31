n = int(input())
count = 1
current = 1

while current < n:
    current += count * 6
    count += 1

print(count)