import sys
sys.setrecursionlimit(10**6)

pre = []
while True:
    try:
        pre.append(int(input()))
    except:
        break

def prepost(start, end):
    if start > end:
        return
    mid = end + 1
    for i in range(start + 1, end + 1):
        if pre[i] > pre[start]:
            mid = i
            break
    prepost(start + 1, mid - 1) 
    prepost(mid, end)
    print(pre[start])


prepost(0, len(pre) - 1)