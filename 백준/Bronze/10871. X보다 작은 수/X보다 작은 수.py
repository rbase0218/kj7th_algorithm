max, target = map(int, input().split())
numbers = list(map(int, input().split()))

for i in range(len(numbers)):
    if target > numbers[i]:
        print(numbers[i], end = ' ')