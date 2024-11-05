if __name__ == "__main__":
    # 입력
    points = []
    for _ in range(4):
        row = list(map(int, input().split()))
        points.append(row)
    
    # 최대 값
    max_value = max(max(row) for row in points)
    
    # 배열 생성
    fill = [ [0] * (max_value + 1) for _ in range(max_value + 1)]
    
    # 채우기 4번 반복
    for i in range(4):
      for y in range(points[i][0], points[i][2]):
          for x in range(points[i][1], points[i][3]):
              fill[y][x] = 1
    
    count = sum(1 for row in fill for num in row if num >= 1)
    print(count)