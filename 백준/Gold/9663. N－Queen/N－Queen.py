count = int(input())

pos = [0] * count
size = count - 1
flag_a = [False] * count
flag_b = [False] * (count * 2)
flag_c = [False] * (count * 2)
sum = 0

def put() -> None:
    global sum
    sum += 1
    return
    
def set(i: int) -> None:
    for j in range(count):
        if (not flag_a[j] 
            and not flag_b[i + j] 
            and not flag_c[i - j + size]):
            pos[i] = j
            if i == size :
                put()
            else:
                flag_a[j] = flag_b[i+j] = flag_c[i - j + size] = True
                set(i + 1)
                flag_a[j] = flag_b[i + j] = flag_c[i - j + size] = False

set(0)

print(sum)