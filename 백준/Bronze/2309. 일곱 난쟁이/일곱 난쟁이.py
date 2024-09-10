from typing import MutableSequence

def sum(a : MutableSequence) -> int:
    acount = 0
    for i in range(len(a)):
        acount += a[i]
    return acount

def reverse_find(a : MutableSequence, b : int):
    length = len(a)
    for i in range(length - 1, -1, -1):
        # 맨 마지막 배열을 잡는다.
        target = a[i]
        
        # 맨 마지막 배열을 제외한 나머지를 돌린다.
        for j in range(length - 1, -1, -1):
            # 동일한 값이 나타날 경우 Catch
            if target + a[j] == b:
                a.remove(target)
                a.remove(a[j])
                return 

    
numbers = [int(input()) for _ in range(9)]
numbers.sort()

reverse_find(numbers, sum(numbers) - 100)

for i in numbers:
    print(i)