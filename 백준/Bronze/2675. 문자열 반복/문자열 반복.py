for _ in range(int(input())):
    data = list(input().split())
    data[0] = int(data[0])

    answer = []

    for i in range(len(data[1])):
        answer.append(data[1][i] * data[0])
        
    print(f"{''.join(answer)}")