n_count = int(input())
n = list(map(int, input().split()))
m_count = int(input())
m = list(map(int, input().split()))

n.sort()

# 1 2 3 4 5
def binary_search(search_array, num, pl, pr) -> int:
    # 찾지 못한 경우
    if pl > pr:
        return 0
    
    # Pivot은 언제나 PL과 PR의 중간 값을 가진다.
    pivot = (pl + pr) // 2
    
    # Pivot에 위치한 값보다 찾는 값이 작다면?
    if search_array[pivot] < num:
        return binary_search(search_array, num, pivot + 1, pr)
    elif search_array[pivot] > num:
        return binary_search(search_array, num, pl, pivot - 1)
    else:
        return 1
    

for i in range(0, m_count):
    print(binary_search(n, m[i], 0, len(n) - 1))