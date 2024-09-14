a = int(input())
b = int(input())
results = []
for i in range(len(str(b)) - 1, -1, -1):
    results.append(int(str(b)[i]) * a)
    print(results[-1])
print(a*b)    