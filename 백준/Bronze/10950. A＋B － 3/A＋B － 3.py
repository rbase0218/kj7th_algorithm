num = int(input())
numbers = [list(input()) for _ in range(num)]

for i in range(num):
    print(int(numbers[i][0]) + int(numbers[i][2]))