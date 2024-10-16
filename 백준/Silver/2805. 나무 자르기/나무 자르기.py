import sys

def binary_search(min_height, max_height, target):
    if min_height > max_height:
        return max_height
    
    pivot = (min_height + max_height) // 2
    count = sum(max(0, tree - pivot) for tree in trees)
    
    if count < target:
        return binary_search(min_height, pivot - 1, target)
    elif count > target:
        return binary_search(pivot + 1, max_height, target)
    else:
        return pivot

if __name__ == "__main__":
    tree_count, need_wood_weight = map(int, input().split())
    trees = list(map(int, input().split()))
    max_height = max(trees)
    
    print(binary_search(0, max_height, need_wood_weight))