numbers = [int(input()) for _ in range(9)]

maximum = numbers[0]
maximum_index = 1

for i in range(0, len(numbers)):
    if maximum < numbers[i]:
        maximum = numbers[i]
        maximum_index = i + 1
        
print(maximum)
print(maximum_index)