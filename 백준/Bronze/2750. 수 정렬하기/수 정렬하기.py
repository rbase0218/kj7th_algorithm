from typing import MutableSequence

def bubble_sort(a: MutableSequence) -> None:
    n = len(a)
    for i in range(n-1):
        for j in range(n - 1, i, -1):
            if a[j - 1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1]

if __name__ == '__main__':
    num = int(input())
    x = [int(input()) for _ in range(num)]
    
    bubble_sort(x)
    
    for i in range(len(x)):
        print(x[i])