import sys

numbers = list(map(int, input().split()))
min = sys.maxsize

if 0 < numbers[0]:
    min = numbers[0]
if min > numbers[1]:
    min = numbers[1]
        
if min > (numbers[2] - numbers[0]):
    min = (numbers[2] - numbers[0])
if min > (numbers[3] - numbers[1]):
    min = (numbers[3] - numbers[1])
        
print(min)